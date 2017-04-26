#!/usr/bin/env python

# merge.py

import json

def main():
    """Example script that merges two sets of data (from two json files)"""
    #
    # Load in both sets
    with open('setA_fruits.json') as file1:
        dataSetA = json.load(file1)
    with open('setB_colors.json') as file2:
        dataSetB = json.load(file2)

    # Use black as the default color
    defaultColor = {"red": 0.0, "green": 0.0, "blue": 0.0}

    # Create a list of just the colornames from set B
    listOfColorNames = [c["colorName"] for c in dataSetB]

    # Create an empty list and fill it with the new (enhanced) fruits
    mergedFruits = []

    for fruit in dataSetA:
        # Is the color of the fruit present in the list of colors?
        thisColor = fruit["color"]
        if thisColor in listOfColorNames:
            # Get the index of the color: the position where the color name is stored in the list of color names.
            # It will be the same position as the complete color dict is stored in set B.
            indexOfColor = listOfColorNames.index(thisColor)
            color = dataSetB[indexOfColor]
        else:
            # If the color is not in the color list, use the default color
            color = defaultColor
            
        # Set all the color properties which we want to merge
        fruit["red"] = color["red"]
        fruit["green"] = color["green"]
        fruit["blue"] = color["blue"]
        # Add each enhanced color to the new list
        mergedFruits.append(fruit)
        
    # Finally save the merged data set as a new json file
    with open('merged_setAB.json', 'w') as outputFile:
    	json.dump(mergedFruits, outputFile, indent=2, sort_keys=True)


if __name__ == '__main__':
    main()