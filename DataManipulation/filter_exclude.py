#!/usr/bin/env python

# filter_exclude.py

import json

def main():
    """Creates a new `exclude_freq.json` file which is not containing martime words"""
    
    # First set the list of filtered words
    filterwords = [
    	"boat",
    	"boats",
    	"captain",
    	"crew",
    	"deck",
    	"fish",
    	"fishermen",
    	"lifevest",
    	"mast",
    	"sail",
    	"sailing",
    	"sea",
    	"ship",
    	"water",
    	"whaling"
    ]
    
    # Read the original json
    with open('word_freq.json') as sourceFile:
        freqlist = json.load(sourceFile)
    
    # Create a new list
    filteredList = []
    
    # Loop over all the entries
    for freqword in freqlist:
        # Loop over all the words in the filter
        # We use a boolean `includedInFilter` to keep track of an occasional match
        # and allow this info to be used to determine if the element should be included in the next query.
        includedInFilter = False
        for filterword in filterwords:
            # Check if the frequency word is for one of the words from the filter
            if freqword['word'] == filterword:
                includedInFilter = True
        # If the frequency word is not part of any filter, add it
        if not includedInFilter:
            filteredList.append(freqword)
                
    # Save the filtered dict as a json file
    with open('incl_freq.json', 'w') as outputFile:
        json.dump(filteredList, outputFile)

if __name__ == '__main__':
    main()