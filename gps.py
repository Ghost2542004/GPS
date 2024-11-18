import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_location', methods=['GET'])
def get_location():
    lat = request.args.get('lat')
    long = request.args.get('long')
    if lat and long:
        # Here you would store the location, for example in a database
        return "Location stored successfully", 200
    return "Error storing location", 400

@app.route('/')
def index():
    return '''
    <html>
    <body>
    <iframe src="https://www.youtube.com" width="480" height="379" style="border:0;" allowfullscreen></iframe>
    <p><a href="https://www.youtube.com">via youtube</a></p>
    <p id="demo"></p>
    <script>
    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition, handleError);
        } else { 
            document.getElementById("demo").innerHTML = "Geolocation is not supported by this browser.";
        }
    }

    function showPosition(position) {
        const url = `/get_location?lat=${encodeURIComponent(position.coords.latitude)}&long=${encodeURIComponent(position.coords.longitude)}`;
        fetch(url)
            .then(response => response.text())
            .then(result => document.getElementById("demo").innerHTML = result)
            .catch(error => document.getElementById("demo").innerHTML = "Error storing location: " + error.message);
    }

    function handleError(error) {
        switch(error.code) {
            case error.PERMISSION_DENIED:
                document.getElementById("demo").innerHTML = "User denied the request for Geolocation.";
                break;
            case error.POSITION_UNAVAILABLE:
                document.getElementById("demo").innerHTML = "Location information is unavailable.";
                break;
            case error.TIMEOUT:
                document.getElementById("demo").innerHTML = "The request to get user location timed out.";
                break;
            default:
                document.getElementById("demo").innerHTML = "An unknown error occurred.";
                break;
        }
    }

    window.onload = getLocation;
    </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
