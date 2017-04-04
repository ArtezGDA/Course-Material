# Scraping Dutch geo-data

These are some notes about how to scrape geographical data from Dutch governmental data sets.

## Getting Public Data from the Government

##### 1. Waardevolle bomen

http://geo1.arnhem.nl/arcgis/services/Openbaar/Waardevolle_bomen/MapServer/WFSServer?request=GetFeature&service=WFS

`> TypeName is mandatory if featureID isn't present in GET requests.`

- python OWSLib?
    - http://geopython.github.io/OWSLib/

Or construct the url yourself

##### 2. Contruct the url

http://geo1.arnhem.nl/arcgis/services/Openbaar/Waardevolle_bomen/MapServer/WFSServer?request=GetFeature&service=WFS&TypeName=Openbaar_Waardevolle_bomen:Waardevolle_bomen

##### 3. Map geo points

What is this?

https://en.wikipedia.org/wiki/Geography_Markup_Language

SRS = Spacial Reference System

`<gml:Envelope srsName="urn:ogc:def:crs:EPSG:6.9:28992">`

- https://www.epsg-registry.org
    - is a type of srs: namely EPSG::28992 = "Amersfoort / RD New"
- How to convert?
    - http://cs2cs.mygeodata.eu
- or with python:
    - http://gis.stackexchange.com/questions/78838/how-to-convert-projected-coordinates-to-lat-lon-using-python
