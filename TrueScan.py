# Imports
from opencage.geocoder import OpenCageGeocode
from math import radians, sin, cos, sqrt, atan2
import plotly.express as px
import plotly.graph_objects as go
import math

# My key to access the OpenCage API
api_key = 'e66b5e8fe7c642e0b7a47d44ee2f151e'
geocoder = OpenCageGeocode(api_key)

# Constants
EARTH_RADIUS_MILES = 3956

def geocode_address(address):
    '''
    Function that returns latitude and longitude, given an address

    Parameters: 
    - address: The address given by the user

    Returns:
    - float: Latitude and longitude of the given address, or None if geocoding fails
    '''
    try:
        # Turn address into lat, lng
        result = geocoder.geocode(address)
        
        if result and len(result):
            # Extract latitude and longitude from the first result
            location = result[0]['geometry']
            return location['lat'], location['lng']
        else:
            return None
    except Exception as e:
        print(f"Error during geocoding: {e}")
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

    # Calculate the distance
    distance = EARTH_RADIUS_MILES * c
    return distance

def create_map(coord_1, coord_2, name1, name2, distance):
    '''
    Function that creates a world map and plots the two coordinates

    Parameters:
    - coord_1: Lat,lon of the first address given
    - coord_2: Lat, lon of the second address given
    - name1: First address that was given
    - name2: Second address that was given
    - distance: The distance between the two points, in miles

    Returns:
    - Scatter_geo plot with two markers
    '''
    # Create a DataFrame with the coordinates
    data = {'Latitude': [coord_1[0], coord_2[0]],
            'Longitude': [coord_1[1], coord_2[1]],
            'Location': [name1, name2]}

    # Create scatter_geo plot
    fig = px.scatter_geo(data, 
                         lat='Latitude', 
                         lon='Longitude',
                         text='Location',
                         projection="natural earth",
                         title="The distance between these two addresses is: " + f"{round(distance, 3)} miles.")

    # Add a line between the two points
    fig.add_trace(go.Scattergeo(
        lat=[coord_1[0], coord_2[0]],
        lon=[coord_1[1], coord_2[1]],
        mode='lines',
        line=dict(width=2, color='black'),
        showlegend=False  # This line won't appear in the legend
    ))

    # Show the figure
    fig.show()

# Main function
def main():

    print("***WELCOME***")

    address1 = input("Please enter the starting address (House Number Street Name, Town, State): ")
    address2 = input("Please enter the ending address (House Number Street Name, Town, State): ")

    coord_a1 = geocode_address(address1)
    coord_a2 = geocode_address(address2)

    if coord_a1 is not None and coord_a2 is not None:
        distance = distance_between(coord_a1[0], coord_a1[1], coord_a2[0], coord_a2[1])
        create_map(coord_a1, coord_a2, address1, address2, distance)
    else:
        print("Error geocoding addresses. Please check your inputs.")

# Run the code
main()
