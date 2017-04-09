#!/usr/bin/env python

# count_word_freq.py

import re
import json
from tqdm import tqdm

def main():
    """Count word frequencies in Moby Dick"""
    
    # Create an empty wordlist
    wordlist = []
    
    # Read the contents of Moby Dick
    with open("corpus.txt") as corpus:
        for line in corpus:
            wordlist += line.lower().split()

    # Remove the first "word"
    wordlist = wordlist[1:]
    
    # Normalize the words by spliting words like "ago--never"
    normlist = []
    splitPattern = re.compile(r'\W+', re.UNICODE)
    for word in wordlist:
        normalizedWords = splitPattern.split(word)
        for normWord in normalizedWords:
            if normWord:
                normlist.append(normWord)
    wordlist = normlist
    
    # Count the frequencies
    # wordFreq = [wordlist.count(w) for w in wordlist]
    wordFreq = []
    for w in tqdm(wordlist):
        wordFreq.append(wordlist.count(w))
    freqDict = dict(zip(wordlist, wordFreq))
    
    # Save the frequency table as JSON
    with open('wordfrequencies.json', 'w') as outfile:
        json.dump(freqDict, outfile)

if __name__ == '__main__':
    main()