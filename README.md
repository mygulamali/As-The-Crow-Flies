# As The Crow Flies

## Synopsis

This is a toy web app that I wrote using [Python][1]/[Flask][2] as part of
a job application for a developer position at a startup in London.  It consists
of a web service and web page that calculate the "as the crow flies" distance
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



#### Remote deployment

The [Flask][2] documentation has some good tutorials about how to deploy a
[Flask][2] web app ([here][7] and [here][8]) on your particular web server
environment.

## License

This project is licensed under the terms and conditions of [The MIT
License][10].  Please see the license.txt file for more details.

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
