# getStreets.py

# Example script that demonstrates how to get the geometry data out of a 'shapefile'
# A shapefile is a combination of .shp, .dbf, and .shx files, describing
# the (vector) shapes of geographic "features" (roads, bridges, lakes, etc)

# The following example deals with roads (in the Netherlands)
# (To make this script work, you'll have to download the shapefile for roads
# in the Netherlands and put these files in the same location as this file.)

# Import the necessary modules to read and parse the geodata
from osgeo import ogr
import json

# Set a driver. The 'ESRI Shapefile' is a standardized format for geodata 
driver = ogr.GetDriverByName('ESRI Shapefile')

# Let the driver open the shapefile
shp = driver.Open(r'roadsData/roads.shp')

# Get the layer from the shapefile.
# A shapefile can contain multiple layers (think separate layers for roads, rivers, train tracks, etc)
# In this case our 'roads.shp' shapefile only contains one layer. We can get just the layer.
layer = shp.GetLayer()


## Investigate the layer a bit

# There is a thing called a "spacial reference", which describes the reference and format in which each
# geometric element is stored.
# In our case the spacial reference is WGS_1984, which is normal latitude, longitude in degrees.
spacialRef = layer.GetSpatialRef()
print(spacialRef)

# The layer definition describes which properties of a feature are stored in the dataset.
# Properties of a feature are details of the feature, not described in the shape itself.
# As we will see shortly, our roads have properties like 'name', 'type of road' and 'maximum speed'.
layerDefinition = layer.GetLayerDefn()

# First get the number of (property) fields in the definition
print(layerDefinition.GetFieldCount())
# 6

# Then loop over all these fields and print their name, their data type and their length 
for i in range(layerDefinition.GetFieldCount()):
	fieldName = layerDefinition.GetFieldDefn(i).GetName()
	fieldType = layerDefinition.GetFieldDefn(i).GetType()
	fieldTypeName = layerDefinition.GetFieldDefn(i).GetFieldTypeName(fieldType)
	fieldWidth = layerDefinition.GetFieldDefn(i).GetWidth()
	print fieldName + " - " + fieldTypeName + " " + str(fieldWidth)
# osm_id - Real 11
# name - String 48
# ref - String 16
# type - String 16
# oneway - Integer 1
# maxspeed - Integer 3



## Investigate the features in the layer

# The "features" in a layer are the separate spacial elements that make up that layer.
# E.g. In a shape layer with bridges, each separate bridge would be a feature

# Get the number of features (Wow, that is a lot!)
nOfFeatures = layer.GetFeatureCount()
print(nOfFeatures)
# 1092235

# Just getting a feature by index (1) is not the most practically way to do if we are looking
# for a specific road, as we just learned there are more than one million roads.

# Therefor, it is more useful to filter on specific feature (by name ... or by type)

# Set a filter. In this case we set a filter by name, to a street on Texel
layer.SetAttributeFilter("type = 'motorway'")

# Then we iterate (loop) through all the features, and print out the name as a check.
print(layer.GetFeatureCount())

streetSegments = []
for feature in layer:
	roadType = feature.GetField("type")
	geometry = feature.GetGeometryRef()
	nPoints = geometry.GetPointCount()
	print "road type: %s, number of points: %d" % (roadType, nPoints)
	segmentPoints = []
	for i in range(geometry.GetPointCount()):
		point = geometry.GetPoint(i)
		pointDict = {}
		pointDict['lon'] = point[0]
		pointDict['lat'] = point[1]
		segmentPoints.append(pointDict)
	streetSegments.append(segmentPoints)

# Export geometry as json
jsonfile = "geometry.json"
with open(jsonfile, 'w') as outputFile:
	json.dump(streetSegments, outputFile)
