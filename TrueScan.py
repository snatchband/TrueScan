# Import the opencage package and math
from opencage.geocoder import OpenCageGeocode
from math import radians, sin, cos, sqrt, atan2
import math

# My key to access the OpenCage API
api_key = 'e66b5e8fe7c642e0b7a47d44ee2f151e'
geocoder = OpenCageGeocode(api_key)

def geocode_address(address):
    '''
    Function that returns latitude and longitude, given an address

    Parameters: 
    - address: The address given by the user

    Returns:
    - float: Latitude and longitude of the given address
    '''
    # Turn address into lat, lng
    result = geocoder.geocode(address)
    
    if result and len(result):
        # Extract latitude and longitude from the first result
        location = result[0]['geometry']
        return location['lat'], location['lng']
    else:
        return None
    
def distance_between(lat1, lon1, lat2, lon2):
    '''
    Function that returns the distance between two given coordinates

    Parameters:
    - lat1: the latitude of the first address
    - lon1: the longitude of the first address
    - lat2: the latitude of the second address
    - lon2: the longitude of the second address

    Returns:
    - float: the distance between the given coordinates in miles
    '''
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Earth radius in miles
    radius = 3956

    # Calculate the distance
    distance = radius * c
    return distance

#Main function
def main():
    print("***WELCOME***")

    address1 = input("Please enter the starting address (House Number Street Name, Town, State): ")
    address2 = input("Please enter the ending address (House Number Street Name, Town, State): ")

    coord_a1 = geocode_address(address1)
    coord_a2 = geocode_address(address2)

    ans = distance_between(coord_a1[0], coord_a1[1], coord_a2[0], coord_a2[1])
    
    print("The distance between the two addresses is approximately " + str(round(ans, 2)) + " miles\n***GOODBYE***")

#Run the code
main()