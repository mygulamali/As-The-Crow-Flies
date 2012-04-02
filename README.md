# As The Crow Flies

## Synopsis

This is a toy web app that I wrote using [Python][1]/[Flask][2] as part of
a job application for a developer position at a startup in London.  It consists
of a web service and web page that calculates the "as the crow flies" distance
between the user's location and [White Bear Yard][3] at 144A Clerkenwell Road,
London, EC1R 5DF, UK.

## Requirements

The following libraries are required to run the web service:

* [Python][1]
* [Flask][2]
* [Requests][4]

The end user is expected to be using a modern W3C compliant browser that
supports the [W3C geolocation specifications][5].  My personal favourite is
[Google Chrome][6].

## Setup

Having downloaded/cloned this project, beginning by edit the server settings
in the `as_the_crow_flies.py` file.  In particular, change the following
variables:

* `HOST`: the IP address or domain name for the web service.
* `PORT`: the port for the web service.
* `DEBUG_MODE`: whether or not [debug mode][9] is switched on.

Then, in the `example.html` file, edit the `url` in the `getDistance` Javascript
function (line 56) to have the same hostname and port number.

#### Local deployment

In a terminal window, navigate to the directory containing this project and
then execute, `python as_the_crow_flies.py`, in order to run the web service.

Then, in another terminal window, in the project directory, execute,
`python -m SimpleHTTPServer`, to begin a web server.  This will inform you where
the HTTP server is being served eg. `Serving HTTP on 0.0.0.0 port 8000 ...`
Navigate to the `example.html` file using the associated URL in your browser
(eg. `http://0.0.0.0:8000/example.html`) to view the web page.

#### Remote deployment

The [Flask][2] documentation has some good tutorials about how to deploy a
[Flask][2] web app ([here][7] and [here][8]) on your particular web server
environment.

## Usage

#### Request

The web service presents a single API endpoint which can be called with a
GET HTTP method:

`http://www.example.com/as_the_crow_flies`

This is called with the following parameters:

<table>
    <tr>
        <th>Parameter</th>
        <th>Example</th>
        <th>Details</th>
    </tr>
    <tr>
        <td><code>q</code></td>
        <td><code>Google Campus, London</code></td>
        <td><strong>required</strong> A query string containing a location.
        This could be a latitude and longitude pair separated by a comma, or an
        address.  This will be geocoded by the
        <a href="https://developers.google.com/maps/documentation/geocoding/">Google
        Maps Geocoding API</a> so it may be a fairly general address.</td>
    </tr>
    <tr>
        <td><code>u</code></td>
        <td><code>miles</code></td>
        <td><strong>optional</strong> A keyword which indicates the units for
        the resulting query.  This may be one of <code>km</code>,
        <code>m</code>, <code>miles</code> or <code>yards</code>.  If it is not
        one of these, or this keyword is ommited, the result defaults to 
        <code>km</code>.</td>
    </tr>
</table>

Thus an example request may be something like:

`http://www.example.com/as_the_crow_flies?q=Google%20Campus%2C%20London&u=miles`

Note: it's always a code idea to URL escape characters in the parameter strings.

#### Response

The web service responds with a JSON response such as:

    {
        "status":
        {
            "message": ...,
            "code": ...
        },
        "result":
        {
            "distance": ...,
            "elapsed": ...,
            "units": ...,
            "address": ...,
            "lat": ...,
            "lng": ...
        }
    }

where each field is as follows:

<table>
    <tr>
        <th>Field</th>
        <th>Details</th>
    </tr>    
    <tr>
        <td><code>message</code></td>
        <td>Message associated with status of response.</td>
    </tr>
    <tr>
        <td><code>code</code></td>
        <td>HTTP response code.</td>
    </tr>
    <tr>
        <td><code>distance</code></td>
        <td>Distance between queried address and [White Bear Yard][3].</td>
    </tr>
    <tr>
        <td><code>elapsed</code></td>
        <td>Number of milliseconds required to process query.  This does not
        include the transit time for sending the request or receiving the
        response.</td>
    </tr>
    <tr>
        <td><code>units</code></td>
        <td>Physical units of the distance value.</td>
    </tr>
    <tr>
        <td><code>address</code></td>
        <td>Formatted address of the queried address.</td>
    </tr>
    <tr>
        <td><code>lat</code></td>
        <td>Latitude of the queried address.</td>
    </tr>
    <tr>
        <td><code>lng</code></td>
        <td>Longitude of the queried address.</td>
    </tr>
</table>

## License

This project is licensed under the terms and conditions of [The MIT
License][10].  Please see the `license.txt` file for more details.

[1]: http://www.python.org/ "Python"
[2]: http://flask.pocoo.org/ "Flask"
[3]: http://whitebearyard.com/ "White Bear Yard"
[4]: http://docs.python-requests.org/en/latest/index.html "Requests"
[5]: http://dev.w3.org/geo/api/spec-source.html "W3C geolocation specifications"
[6]: https://www.google.com/chrome "Google Chrome"
[7]: http://flask.pocoo.org/docs/deploying/ "Deployment options for Flask"
[8]: http://flask.pocoo.org/docs/quickstart/#quickstart-deployment "Deploying to a web server"
[9]: http://flask.pocoo.org/docs/quickstart/#debug-mode "Flask debug mode"
[10]: http://www.opensource.org/licenses/mit-license.php "The MIT License"
