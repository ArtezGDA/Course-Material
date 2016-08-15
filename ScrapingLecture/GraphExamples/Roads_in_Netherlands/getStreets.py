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

# To investigate further one of these "features" (roads in our case),
# just take a random one. (The second feature, -the feature with index 1- is sort of random)
feature = layer.GetFeature(1)

print(feature.GetField('name'))
# 'Pieter Bernagiestraat'

# Get the geometry
geometry = feature.GetGeometryRef()

# Print the center of the geometry (officially that is called a centroid)
print(geometry.Centroid().ExportToWkt())
# 'POINT (5.119420415251341 52.07722473616613)'

# Get the number of points in the geometry
print(geometry.GetPointCount())
# 9

# Just as an example, print second point. (Ah, it is a tuple, of longitude, latitude and ... 0, (for height?) )
print(geometry.GetPoint(1))
# (5.1181232, 52.0775645, 0.0)



# Just getting a feature by index (1) is not the most practically way to do if we are looking
# for a specific road, as we just learned there are more than one million roads.

# Therefor, it is more useful to filter on specific feature (by name ... or by type)

# Set a filter. In this case we set a filter by name, to a street on Texel
layer.SetAttributeFilter("name = 'Achtertune'")

# Then we iterate (loop) through all the features, and print out the name as a check.
for feature in layer:
	print feature.GetField("name")
# Achtertune
# Achtertune
# Achtertune
# Achtertune

# Interestingly, it turns out the dataset contains 4(!) features for the Achtertune street,
# and not just one. It actually turns out that these different features are all "road segments"
# of the same roads, and are adjacent to each other.

# If we try this a second time, it results to nothing
for feature in layer:
	print feature.GetField("name")
#
# (Doesn't print anything anymore, the second time,
# as the filter doesn't result to more than the set already returned)


# Set the filter again
layer.SetAttributeFilter("name = 'Achtertune'")

# Now, lets print some more useful information about the road segments:
# - The type of road (highway, main road, secondary road, or smaller)
# - The number of points of the segment
# - The coordinate of each point in each segment

streetSegments = []

for feature in layer:
	roadType = feature.GetField("type")
	geometry = feature.GetGeometryRef()
	nPoints = geometry.GetPointCount()
	print "road type: %s, number of points: %d" % (roadType, nPoints)
	segmentPoints = []
	for i in range(geometry.GetPointCount()):
		point = geometry.GetPoint(i)
		print "\t%s" % (point,)
		pointDict = {}
		pointDict['lon'] = point[0]
		pointDict['lat'] = point[1]
		segmentPoints.append(pointDict)
	streetSegments.append(segmentPoints)	

# Export geometry as json
jsonfile = "geometry.json"
with open(jsonfile, 'w') as outputFile:
	json.dump(streetSegments, outputFile)
