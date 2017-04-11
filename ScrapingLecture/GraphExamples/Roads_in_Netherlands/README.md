# Get highways in the Netherlands example

To get these examples running:

- Download the '*shapefile*' for all the roads in the Netherlands from http://www.mapcruzin.com/free-netherlands-arcgis-maps-shapefiles.htm
- Move the shapefile files to a directory called `roadsData` within this directory
- Install `gdal` as a python module

### Installing `gdal`

On my machine (with El Capitan), it turned out quite a hassle to install the *gdal* module into the system's default python installation. Therefor I used Homebrew (http://brew.sh) to first install its own version of python and then gdal.

`brew install python`

`brew install gdal`


