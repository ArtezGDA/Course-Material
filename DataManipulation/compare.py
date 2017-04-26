#!/usr/bin/env python

# compare.py

import json

def main():
    """Example script that compares two json files"""
    #
    # Load in both sets
    #
    with open('setA_fruits.json') as file1:
        dataSetA = json.load(file1)
    with open('setB_colors.json') as file2:
        dataSetB = json.load(file2)
    #
    # Start with formal comparison
    print "setA:", len(dataSetA)
    print "setB:", len(dataSetB)
    #
    print "------------------------------"
    # Checking which are in set A, but missing in set B
    #
    # Create a list of just the colornames from set B
    listOfColorNames = [c["colorName"] for c in dataSetB]
    # 
    # Create an empty list and fill it with all the ummatched fruits
    unmatchedFruits = []
    for fruit in dataSetA:
        if not fruit["color"] in listOfColorNames:
            unmatchedFruits.append(fruit)
    #
    # Report about unmatched fruits
    print "Number of unmatched fruits:", len(unmatchedFruits)
    print "missing colors:", [f["color"] for f in unmatchedFruits]
    #
    print "------------------------------"
    # Checking which are in set B, but missing in set A
    #
    # Create a list of just color (names) from set A
    listOfFruitColors = [c["color"] for c in dataSetA]
    #
    # Create an empty list and fill it with all the ununsed colors
    unusedColors = []
    for color in dataSetB:
        if not color["colorName"] in listOfFruitColors:
            unusedColors.append(color)
    #
    # Report about unused colors
    print "Number of unused colors:", len(unusedColors)
    print "unused colors:", [c["colorName"] for c in unusedColors]
    

if __name__ == '__main__':
    main()