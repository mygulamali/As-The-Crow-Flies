#!/usr/bin/env python

from math import sin, cos, atan2, sqrt, pi
import json
import urllib
import requests
import time
from flask import Flask, request

# conversion factor from degrees to radians
DEGREES2RADIANS = pi/180.0

# conversion factor from kilometres to miles
KM2MILES = 6.21371192e-1

# conversion factor from kilometres to yards
KM2YARDS = 1.0936133e3

# mean radius of the Earth [km]
RADIUS_EARTH = 6.371e3

# location of White Bear Yard, 144a Clerkenwell Road, London, EC1R 5DF, UK.
WHITE_BEAR_YARD = {'lat': 51.52219930, 'lng': -0.10976180}

def geodesic_distance(point_A, point_B):
    """Geodesic distance between two points on the Earth."""
    lat_A, lng_A = point_A['lat']*DEGREES2RADIANS, point_A['lng']*DEGREES2RADIANS
    lat_B, lng_B = point_B['lat']*DEGREES2RADIANS, point_B['lng']*DEGREES2RADIANS
    # Vincenty's formula eg. http://en.wikipedia.org/wiki/Great-circle_distance
    dl = abs(lng_B - lng_A)
    a = cos(lat_B)*sin(dl)
    b = cos(lat_A)*sin(lat_B)-sin(lat_A)*cos(lat_B)*cos(dl)
    c = sin(lat_A)*sin(lat_B)+cos(lat_A)*cos(lat_B)*cos(dl)
    return RADIUS_EARTH*atan2(sqrt(a*a+b*b),c)

def geocode_address(address):
    """Latitude and longitude of specified address using Google Maps Geocoding API."""
    url = 'http://maps.googleapis.com/maps/api/geocode/json?'   
    parameters = {'address': address, 'sensor': 'false'}
    response = requests.get(url + urllib.urlencode(parameters))
    if (response.status_code==200):
        return json.loads(response.content)
    return None

def get_distance(lat,lng,units=None):
    """Return distance between specified position and White Bear Yard in specified units."""
    distance = geodesic_distance(WHITE_BEAR_YARD,{'lat': lat, 'lng': lng})
    if units=='m':
        return distance*1.0e3
    elif units=='yards':
        return distance*KM2YARDS
    elif units=='miles':
        return distance*KM2MILES
    return distance

def parse_query(args):
  """Parse request query and return parameters."""
  address = args.get('q')
  units = args.get('u')
  return (address, units)

def create_response(code,message,lat,lng,address,distance,units):
    """Create response using specified parameters."""
    return {'status': {'code': code,
                       'message': message},
            'result': {'lat': lat,
                       'lng': lng,
                       'address': address,
                       'distance': distance,
                       'units': units,
                       'elapsed': 0.0}}

# ----------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/as_the_crow_flies")
def as_the_crow_flies():
    t_start = time.time()
    address, units = parse_query(request.args)
    if address:
        geocoded = geocode_address(address)
        if (geocoded) and (len(geocoded[u'results'])>0):
            lat = geocoded[u'results'][0][u'geometry'][u'location'][u'lat']
            lng = geocoded[u'results'][0][u'geometry'][u'location'][u'lng']
            formatted_address = geocoded[u'results'][0][u'formatted_address']
            response = create_response(200,
                                       'Successful query',
                                       lat,
                                       lng,
                                       formatted_address,
                                       get_distance(lat,lng,units),
                                       units if units else 'km')
        else:
            response = create_response(400,
                                       'Query could not be geocoded',
                                       '',
                                       '',
                                       address,
                                       '',
                                       'km')
    else:
        response = create_response(204,
                                   'No valid query made',
                                   WHITE_BEAR_YARD['lat'],
                                   WHITE_BEAR_YARD['lng'],
                                   '144A Clerkenwell Rd, London, Greater London EC1R 5DF, UK',
                                   0.0,
                                   'km')
    response['result']['elapsed'] = (time.time() - t_start)*1.0e3
    return json.dumps(response)

@app.errorhandler(404)
def page_not_found(error):
    t_start = time.time()
    response = create_response(404,
                               'No such endpoint',
                               '',
                               '',
                               '',
                               '',
                               '')
    response['result']['elapsed'] = (time.time() - t_start)*1.0e3
    return json.dumps(response), 404

# ----------------------------------------------------------------------------

if __name__=="__main__":
  app.run(debug=True)

