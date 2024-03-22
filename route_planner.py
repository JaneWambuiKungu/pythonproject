import requests

def request_route_and_estimates(start_location, target_location, transport_means):
    
    api_key = 'AIzaSyCoh98cSNkWUiGOdv2qqeq9ExbmfmkUT2E'
    url = 'https://maps.googleapis.com/maps/api/directions/json'

    params = {
        'origin': f"{start_location['street']}, {start_location['city']}, {start_location['postalCode']}, {start_location['country']}",
        'destination': f"{target_location['street']}, {target_location['city']}, {target_location['postalCode']}, {target_location['country']}",
        'mode': transport_means.lower(),
        'key': api_key
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return 'Error', response.status_code

    directions = response.json()

    # Extract the relevant information from the directions response
    # and format it according to your RouteDetails schema
    # ...

    return route_details
