import pylab as pl 
import os
import json
import sys
import numpy as np
import pandas as pd 
try:
	import urllib2 as urllib
except ImportError:
	import urllib.request as urllib 

bus_line = str(sys.argv[2])
api_key = str(sys.argv[1])
bus_line_file_name = str(sys.argv[3])

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + api_key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + bus_line

response = urllib.urlopen(url)
data = response.read().decode('utf-8')
data = json.loads(data)

bus_data = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

out_df = pd.DataFrame()

for i in bus_data:
	add_list = []
	#Latitude
	add_list.append(str(i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']))
	#Longitude
	add_list.append(str(i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
	#Destination Name
	#Presentable Distance
	if (len(i['MonitoredVehicleJourney']['OnwardCalls']) == 0):
		add_list.append('N/A')
		add_list.append('N/A')
	else:
		add_list.append(str(i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']))
		add_list.append(str(i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']))
	
	add_df = pd.DataFrame(data=[add_list])
	out_df = pd.concat([out_df,add_df], axis=0)

out_df.columns = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']
out_df.reset_index()
out_df.to_csv(bus_line_file_name)






