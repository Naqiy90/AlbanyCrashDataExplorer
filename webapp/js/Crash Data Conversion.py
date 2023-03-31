import pandas as pd
import geopandas as gpd

# Load the DBF file into a GeoDataFrame
gdf = gpd.read_file("C:\Users\Naqiy\Documents\GitHub\CrashDataExplorer\Albany Crash Data.dbf")

# Convert the GeoDataFrame to a GeoJSON file
gdf.to_file("C:\Users\Naqiy\Documents\GitHub\CrashDataExplorer\Albany Crash Data.GeoJSON", driver='GeoJSON')

# Name of file to create as output
ped_file_output = "webapp/data/cde_ped.js"
bike_file_output = "webapp/data/cde_bike.js"
# Name of js variable that contains JSON
ped_js_variable = "PedCrashes"
bike_js_variable = "BikeCrashes"



function getSeverityLabel(x) {
	if (invertSeverity) {
		x = invertSeverityValues(x);
	}
	if (x == 1) { return "Property Damage" }
	else if (x == 2) { return "Possible Injury" }
	else if (x == 3) { return "Non-Incapacitating Injury" }
	else if (x == 4) { return "Incapacitating Injury" }
	else if (x == 5) { return "Fatal" }
	else { return x }

#Created on Fri Mar 24 08:13:44 2023

#@author: Naqiy

