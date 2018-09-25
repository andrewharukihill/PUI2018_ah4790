import pylab as pl 
import os
import json
import sys
try:
	import urllib2 as urllib
except ImportError:
	import urllib.request as urllib 

bus_line = str(sys.argv[2])
api_key = str(sys.argv[1])

print("Bus Line : " + bus_line)

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + api_key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + bus_line

response = urllib.urlopen(url)
data = response.read().decode('utf-8')
data = json.loads(data)

bus_data = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
print("Number of Active Buses : " + str(len(bus_data)))

bus_number = 0
for i in bus_data:
	print("Bus " + str(bus_number) + " is at latitude " + str(i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']) +
		" and longitude " + str(i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
	bus_number += 1

