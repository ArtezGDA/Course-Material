#!/usr/bin/python

# analyze_populations.py

import json
from tqdm import tqdm

def main():
	"""Analyze the city populations data."""
	# Get the populations data from our json file
	with open("city_populations.json", 'r') as inputFile:
	   citiesData = json.load(inputFile)
	print "Analyzing %d countries" % (len(citiesData))
	numberOfCities = 0
	withPopulationData = 0
	# Loop through all contries and all cities
	for country in citiesData:
		if country.has_key('cities'):
			for city in country['cities']:
				numberOfCities += 1
				# Only if there is populationInfo
				if city.has_key('populationInfo'):
					withPopulationData += 1
	print "with %d cities, of which %d have population information" % (numberOfCities, withPopulationData)
	print "-----------------------------"
	# Create a dictionary of population info keys
	populationKeys = {}
	# Loop again through all the countries and all cities
	for country in citiesData:
		if country.has_key('cities'):
			for city in country['cities']:
				# Only if there is populationInfo
				if city.has_key('populationInfo'):
					# Loop through all the keys in populationInfo
					for key in city['populationInfo'].keys():
						# See if we already have this key
						if key in populationKeys.keys():
							# Increase the number of occurances
							populationKeys[key] += 1
						else:
							# Create the key and set its occurance to 1
							populationKeys[key] = 1
	# Print the keys alphabetically sorted
	for key in sorted(populationKeys.keys()):
		print "%s: %s" % (key, populationKeys[key])
	print "-----------------------------"
	# Print the keys alphabetically sorted by occurence
	for key, value in sorted(populationKeys.iteritems(), key=lambda (k, v): (v ,k), reverse=True):
		print "%s: %s" % (key, value)
	
if __name__ == '__main__':
	main()
	
	