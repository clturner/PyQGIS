#!/env/bin/env python

"""
Counts the number of points in a points layer that fall within every feature 
of a polygon layer.

Creates a new polygon shapefile with an attribute column with resulting count of
points within each polygon feature

"""
from qgis.core import *
import processing

polygon_layer = "<PATH TO POLYGON LAYER>"
point_layer = "<PATH TO POINTS LAYER>"
attribute_column_name = 'NUMPOINTS'
Result = "<PATH TO NEW SHAPEFILE>"
processing.runalg("qgis:countpointsinpolygon", polygon_layer, point_layer, attribute_column_name, Result)
