#!/usr/bin/env python

# flatten.py

import json

def main():
    """Reads the nested json file and stores a flattened version of the same data"""
    # Load the original data from file
    with open('nested_structure.json', 'r') as inputFile:
    	nestedData = json.load(inputFile)
    
    # Create an empty list to store the data in
    flattened = []
    
    # Loop over each year
    for yearData in nestedData['years']:
        year = yearData['year']
        # Loop over each month
        for monthData in yearData['months']:
            month = monthData['month']
            # Loop over each day
            for dayData in monthData['days']:
                day = dayData['day']
                # Get the data
                data = dayData['data']
                # Add date (year, month and day) information to the data
                data['year'] = year
                data['month'] = month
                data['day'] = day
                # Add the data object to the flat list
                flattened.append(data)
    
    # Save the data to a new json file
    with open('flattened_data.json', 'w') as outputFile:
    	json.dump(flattened, outputFile, indent=2, sort_keys=True)


if __name__ == '__main__':
    main()