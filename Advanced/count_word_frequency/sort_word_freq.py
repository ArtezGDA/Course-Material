#!/usr/bin/env python

# sorted_frequency.py

# NOTE: this script makes only sense to run after a `wordfrequencies.json` was created with the `count_word_freq.py`

import json

def main():
    """This script takes the wordfrequencies.json and turns this into a sorted frequency list"""
    
    # Open the frequency dict json
    with open('wordfrequencies.json') as infile:
        freqDict = json.load(infile)

    # Sort the on frequency
    freqList = [(freqDict[k], k) for k in freqDict]
    freqList.sort()
    freqList.reverse()
    
    # create a list of dicts
    dictList = [{'word': w[1], 'freq': w[0]} for w in freqList]
    
    # Save the list as json
    with open('sorted_frequencies.json', 'w') as outfile:
        json.dump(dictList, outfile)
    
    
if __name__ == '__main__':
    main()