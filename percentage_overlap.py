#!/env/bin/env python

"""
Calculates the percent cover of every feature in an input layer by every feature in an overlap layer.
Prints percent cover of every feature in overlap layer and total cover of all features in input layer by cover layer
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

#Pointer to a registry
registry = QgsMapLayerRegistry.instance()

#Store layers in registry
layer1 = registry.mapLayersByName('<INPUT LAYER>')
layer2 = registry.mapLayersByName('<OVERLAP LAYER>')

#Iterate through layers and store all features in a list
feats_layer1 = [ feat for feat in layer1[0].getFeatures() ]
feats_layer2 = [ feat for feat in layer2[0].getFeatures() ]

#Do ellipsoidal math
area = QgsDistanceArea()
area.setEllipsoid('WGS84')
area.setEllipsoidalMode(True)
area.computeAreaInit()

#Iterate through all features in feats_layer1 and calculate area
for feat1 in feats_layer1:
    boundary = feat1
    area = QgsDistanceArea()
    areas1 = area.measurePolygon(boundary.geometry().asPolygon()[0])
    add_list = []

    #Iterate through all features in feats_layer2 and calculate area
    for feat2 in feats_layer2:
        boundary = feat2
        area = QgsDistanceArea()
        areas2 = area.measurePolygon(feat2.geometry().asPolygon()[0])
        #Check if feature in feat_layer2 for overlap with feature in feat_layer1
        if feat1.geometry().intersects(feat2.geometry()):
            intersection = feat1.geometry().intersection(feat2.geometry())
            for inter in intersection.asPolygon():
                #Calculate percent cover
                p_cover = area.measurePolygon(inter)/areas1
                #Add multiple overlaps to a list
                add_list.append(p_cover)
                print "segment number", feat1['<INSERT ATTRIBUTE COLUMN NAME>'], "forest patch id", feat2['<INSERT ATTRIBUTE COLUMN NAME>']
                print "percent cover is ", p_cover

    #After iterating through all features in feats_layer2 calculate total of all overlapping layers stored in the list                                       
    if feat2['<INSERT ATTRIBUTE COLUMN NAME>'] == long(len(feats_layer2)):
        print "The sum of all patches covering segment ", feat1['<INSERT ATTRIBUTE COLUMN NAME>'], "is ", sum(add_list), "\n"
