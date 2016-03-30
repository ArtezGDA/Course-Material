#!/usr/bin/python

# scrape_wiki_city_population.py

from bs4 import BeautifulSoup
import urllib
import json
from time import sleep
from tqdm import tqdm

def main():
	"""Scrapes population from a city page, from a list of cities (per country)"""
	#
	# First get all the cities
	with open("cities.json", 'r') as inputFile:
	   citiesData = json.load(inputFile)
	#
	# The citiesData is a nested list of countries with cities
	numberOfCities = 0
	pBarCountries = tqdm(citiesData, leave=True, nested=True)
	for c in pBarCountries:
		country = c['country']
		if c.has_key('cities'):
			cities = c['cities']
			pBarCountries.set_description("Processing %s" % country)
			pBarCities = tqdm(cities[:5], leave=True, nested=True)
			for city in pBarCities:
				# Open the city page
				r = urllib.urlopen(city['url']).read()
				soup = BeautifulSoup(r, "html.parser")
				# Get the infobox table
				infoBox = soup.find('table', class_="infobox")
				# Get all mergedTopRows
				mergedTopRows = infoBox.findAll('tr', class_="mergedtoprow")
				# Find the Population mergedTopRow
				populationMergedTopRow = None
				for m in mergedTopRows:
					text = m.text.strip()
					if text.startswith("Population"):
						populationMergedTopRow = m
						break
				if populationMergedTopRow:
					pDict = {}
					foundPopulation = False
					for tr in populationMergedTopRow.findNextSiblings('tr'):
						if 'mergedrow' in tr['class']:
							populationKey = tr.find('th').text.strip().strip(u'\xa0\u2022\xa0')
							if populationKey:
								populationValue = tr.find('td').text.strip()
								if populationValue:
									# Add the key and value to a sub - dict
									pDict[populationKey] = populationValue
									# Keep track of whether population was found
									foundPopulation = True
						else:
							break
					if foundPopulation:
						# increment a counter
						numberOfCities += 1
						# Add the info to the city data
						city['populationInfo'] = pDict
	# Finally: save a file, with all cities by countries
	with open("city_populations.json", 'w') as outputFile:
	   json.dump(citiesData, outputFile, indent=2)
	print "Found %d cities with population" % (numberOfCities)
	

if __name__ == '__main__':
	main()