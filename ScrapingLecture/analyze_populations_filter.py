#!/usr/bin/python

# analyze_populations.py

import json
from tqdm import tqdm

def keysFilter():
	keysList = [
		# Total is prefered
		{'match': "Total", 'startsWith': False},
		# Urban (and relevant alterations)
		{'match': "Urban", 'startsWith': False},
		{'match': "Urban area", 'startsWith': False},
		{'match': "Urban[", 'startsWith': True},
		{'match': "Urban (", 'startsWith': True},
		# Metro (and relevant alterations)
		{'match': "Metro", 'startsWith': False},
		{'match': "Metro region", 'startsWith': False},
		{'match': "Metro[", 'startsWith': True},
		{'match': "Metro (", 'startsWith': True},
		{'match': "Metropolis", 'startsWith': True},
		{'match': "Metropollis", 'startsWith': False},
		{'match': "Metropolitan", 'startsWith': False},
		{'match': "Metropolitan Area", 'startsWith': False},
		{'match': "Metropolitan City", 'startsWith': True},
		{'match': "Metropolitan city", 'startsWith': False},
		{'match': "Metropolitan region", 'startsWith': False},
		# Agglomeration & District
		{'match': "Agglomeration", 'startsWith': False},
		{'match': "District", 'startsWith': False},
		# Estimate
		{'match': "Estimate (", 'startsWith': True},
		# Municipality
		{'match': "Municipality", 'startsWith': False},
		{'match': "municipality", 'startsWith': False},
		{'match': "Municipality and city", 'startsWith': False},
		{'match': "Municipality and town", 'startsWith': False},
		{'match': "Municipality unit", 'startsWith': False},
		{'match': "Municipal Districts", 'startsWith': False},
		{'match': "Municipal unit", 'startsWith': False},
		{'match': "Municipio", 'startsWith': False},
		# City
		{'match': "city", 'startsWith': False},
		{'match': "City", 'startsWith': False},
		{'match': "City Total", 'startsWith': False},
		{'match': "city District Capital", 'startsWith': False},
		{'match': "City and commune", 'startsWith': False},
		{'match': "City and autonomous district", 'startsWith': False},
		{'match': "City and municipality", 'startsWith': False},
		# Town and others
		{'match': "Town", 'startsWith': False},
		{'match': "Administrative unit", 'startsWith': False},
		{'match': "County-level city", 'startsWith': False},
		{'match': "Capital", 'startsWith': False},
		{'match': "Canton", 'startsWith': False},
		{'match': "Prefecture-level city", 'startsWith': False},
		{'match': "Borough", 'startsWith': False},
		{'match': "Jurisdiction", 'startsWith': False},
		{'match': "Territorial", 'startsWith': False},
		{'match': "(2014)", 'startsWith': False},
		{'match': "Municipality of Colombia", 'startsWith': False},
		{'match': "Temburong District", 'startsWith': False},
		{'match': "Miri City", 'startsWith': False},
	]
	return keysList

def main():
	"""Analyze the city populations data."""
	# Get the populations data from our json file
	with open("city_populations.json", 'r') as inputFile:
	   citiesData = json.load(inputFile)
	print "Analyzing %d countries" % (len(citiesData))
	numberOfCities = 0
	withPopulationData = 0
	withoutMatchingKeys = 0
	withIgnoredKeys = 0
	matchingKeys = []
	keyFilters = keysFilter()
	ignoreKeys = ['Demonym', 'Density', u'\u2013 density']
	# Loop through all contries and all cities
	for country in citiesData:
		if country.has_key('cities'):
			for city in country['cities']:
				numberOfCities += 1
				# Only if there is populationInfo
				if city.has_key('populationInfo'):
					# Loop through all the keys in populationInfo
					withPopulationData += 1
					matchingKeyFound = False
					for key in city['populationInfo'].keys():
						# Loop through all our keys in the filter
						for f in keyFilters:
							if f['startsWith']:
								# Matches if the key starts with the pattern
								if key.startswith(f['match']):
									matchingKeyFound = True
									break
							else:
								# Should match exact
								if key == f['match']:
									matchingKeyFound = True
									break
						if matchingKeyFound:
							if not key in matchingKeys:
								matchingKeys.append(key)
							break
					if not matchingKeyFound:
						# If there is only one key and it is in our list to be ignored, then ignore it
						notMatchingOrUnknownKeys = city['populationInfo'].keys()
						if len(notMatchingOrUnknownKeys) == 1 and notMatchingOrUnknownKeys[0] in ignoreKeys:
							withIgnoredKeys += 1
						else:
							withoutMatchingKeys += 1
							print "Matching key not found for %s. dict: %s" % (city['name'], city['populationInfo'])
	# Print the results
	print "-----------------------------"
	print "with %d cities, of which %d have population information" % (numberOfCities, withPopulationData)
	print "without matching keys: %d (With only a key to be ignored: %d)" % (withoutMatchingKeys, withIgnoredKeys)
	print "-----------------------------"
	print "matched keys:"
	print matchingKeys
	#
	
if __name__ == '__main__':
	main()
	
	