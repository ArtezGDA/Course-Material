#!/usr/bin/env python

import json

def commonWords():
    """Returns a list of common english words"""
    commonList = ['a', 'about', 'above', 'across', 'after', 'afterwards']
    commonList += ['again', 'against', 'all', 'almost', 'alone', 'along']
    commonList += ['already', 'also', 'although', 'always', 'am', 'among']
    commonList += ['amongst', 'amoungst', 'amount', 'an', 'and', 'another']
    commonList += ['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere']
    commonList += ['are', 'around', 'as', 'at', 'back', 'be', 'became']
    commonList += ['because', 'become', 'becomes', 'becoming', 'been']
    commonList += ['before', 'beforehand', 'behind', 'being', 'below']
    commonList += ['beside', 'besides', 'between', 'beyond', 'bill', 'both']
    commonList += ['bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant']
    commonList += ['co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de']
    commonList += ['describe', 'detail', 'did', 'do', 'done', 'down', 'due']
    commonList += ['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else']
    commonList += ['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever']
    commonList += ['every', 'everyone', 'everything', 'everywhere', 'except']
    commonList += ['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first']
    commonList += ['five', 'for', 'former', 'formerly', 'forty', 'found']
    commonList += ['four', 'from', 'front', 'full', 'further', 'get', 'give']
    commonList += ['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her']
    commonList += ['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers']
    commonList += ['herself', 'him', 'himself', 'his', 'how', 'however']
    commonList += ['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed']
    commonList += ['interest', 'into', 'is', 'it', 'its', 'itself', 'keep']
    commonList += ['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made']
    commonList += ['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine']
    commonList += ['more', 'moreover', 'most', 'mostly', 'move', 'much']
    commonList += ['must', 'my', 'myself', 'name', 'namely', 'neither', 'never']
    commonList += ['nevertheless', 'next', 'nine', 'no', 'nobody', 'none']
    commonList += ['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of']
    commonList += ['off', 'often', 'on','once', 'one', 'only', 'onto', 'or']
    commonList += ['other', 'others', 'otherwise', 'our', 'ours', 'ourselves']
    commonList += ['out', 'over', 'own', 'part', 'per', 'perhaps', 'please']
    commonList += ['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed']
    commonList += ['seeming', 'seems', 'serious', 'several', 'she', 'should']
    commonList += ['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so']
    commonList += ['some', 'somehow', 'someone', 'something', 'sometime']
    commonList += ['sometimes', 'somewhere', 'still', 'such', 'system', 'take']
    commonList += ['ten', 'than', 'that', 'the', 'their', 'them', 'themselves']
    commonList += ['then', 'thence', 'there', 'thereafter', 'thereby']
    commonList += ['therefore', 'therein', 'thereupon', 'these', 'they']
    commonList += ['thick', 'thin', 'third', 'this', 'those', 'though', 'three']
    commonList += ['three', 'through', 'throughout', 'thru', 'thus', 'to']
    commonList += ['together', 'too', 'top', 'toward', 'towards', 'twelve']
    commonList += ['twenty', 'two', 'un', 'under', 'until', 'up', 'upon']
    commonList += ['us', 'very', 'via', 'was', 'we', 'well', 'were', 'what']
    commonList += ['whatever', 'when', 'whence', 'whenever', 'where']
    commonList += ['whereafter', 'whereas', 'whereby', 'wherein', 'whereupon']
    commonList += ['wherever', 'whether', 'which', 'while', 'whither', 'who']
    commonList += ['whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with']
    commonList += ['within', 'without', 'would', 'yet', 'you', 'your']
    commonList += ['yours', 'yourself', 'yourselves']
    return commonList

def main():
    """The script removes all the common english words from a word frequency list.
    NOTE: this script makes only sense to run with a `wordfrequencies.json` present in the same directory
    """
    
    # Open the frequency dict json
    with open('wordfrequencies.json') as infile:
        freqDict = json.load(infile)

    # Sort the on frequency
    freqList = [(freqDict[k], k) for k in freqDict]
    freqList.sort()
    freqList.reverse()
    
    
    # Filter out the common english words
    common = commonWords()
    filteredList = [w for w in freqList if w[1] not in common]    
    
    # create a list of dicts
    dictList = [{'word': w[1], 'freq': w[0]} for w in filteredList]
    
    # Save the list as json
    with open('sorted_filtered_frequencies.json', 'w') as outfile:
        json.dump(dictList, outfile)
    

if __name__ == '__main__':
    main()