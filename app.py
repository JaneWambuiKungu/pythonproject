from flask import Flask, request, jsonify
app = Flask(__name__)
import googlemaps
gmaps = googlemaps.Client(key='AIzaSyCoh98cSNkWUiGOdv2qqeq9ExbmfmkUT2E')

@app.route('/route_planner', methods=['POST'])

def request_route_and_estimates():
    # Deserialize the incoming request body to the expected format
    data = request.json
    start_location = data['startLocation']
    target_location = data['targetLocation']
    transport_means = data['transportMeans']

    # Here you'd call your route planner adapter which uses the Google Maps service
    # Since we're assuming this part is already written, we'll simulate it
    # You should replace this with actual calls to Google Maps API
    route_details = {
        "estimatedTime": "1 hour",
        "distance": "10 miles",
        "waypoints": []
    }

    # Serialize the route_details into a JSON response and return it
    return jsonify(route_details), 200


    if __name__ == '__main__':
        app.run(debug=True)

