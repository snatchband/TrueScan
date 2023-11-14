TrueSpan is an easy-to-use app that will tell you the distance between two addresses on earth.

TrueSpan uses the OpenCage API to convert addresses into latitude and longitude. 
Then it uses the Haversine formula to determine the great-circle distance between the two latitudes and longitudes.
It will then return the distance between the given addresses, in terms of miles.

**INSTALL INSTRUCTIONS**
1. Make sure that you have Python Version 3 installed on your computer.
2. Open your command line, and paste "pip install -r requirements.txt" 

The code of TrueSpan works through two main functions. 
First, there is the geocode_address() function on line 10. 
This function uses the OpenCage API to take the addresses given by the user and convert them into latitude and longitude. 
Second, there is the distance_between() funtion on line 30. 
This function uses the Haversine formula to find the distance between the two addresses in terms of radians.
This is important because the earth is a sphere, and finding the great-cirlce distance between the two addresses, in terms of radians, is the most accurate. 
It then converts the answer in radians to miles, so that it can be easily understood by everyone. 
Finally, on line 60, the main() function prompts the user for their inputs and passes them through both of these functions. 

**FUTURE PLANS**
The future for TrueSpan is brighter than ever. 
I can see TrueSpan being used in a Google Maps extension to tell users the great-circle distance between two addresses.
Right now, Google Maps can tell you the great-circle distance using a very clunky pin dropping system.
I can improve upon this by creating an extension that adds a button that allows for two inputs, instead of dragging around a pin.
TrueSpan's job in this extension will be to take the two inputs from the user to find the distance between them.
The extension will have added UI functionality to give a visual representation of the great-circle distance, using Google Maps.  