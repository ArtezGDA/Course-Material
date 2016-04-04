#!/usr/bin/python

# filter_populations.py

import re
import json
from tqdm import tqdm

numberPattern = re.compile(r'[0-9,]+')

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
	"""Filter the city populations data and coalesce into a single value"""
	# Get the populations data from our json file
	with open("city_populations.json", 'r') as inputFile:
	   citiesData = json.load(inputFile)
	print "Analyzing %d countries" % (len(citiesData))
	numberOfCities = 0
	withPopulationData = 0
	keyFilters = keysFilter()
	# Loop through all contries and all cities
	for country in citiesData:
		if country.has_key('cities'):
			for city in country['cities']:
				numberOfCities += 1
				# Only if there is populationInfo
				if city.has_key('populationInfo'):
					# Loop through all the keys in populationInfo
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
							break
					if matchingKeyFound:
						# Get the population value
						populationValue = city['populationInfo'][key]
						m = numberPattern.search(populationValue)
						if m:
							numValue = m.group()
							valueWithoutCommas = numValue.replace(',', '')
							if valueWithoutCommas:
								intValue = int(valueWithoutCommas)
								withPopulationData += 1
								city['population'] = intValue
				# Remove the old populationInfo dictionary, if there was a populationInfo key present
				if city.has_key('populationInfo'):
					del city['populationInfo']
	# Save into a new file
	with open("population_of_cities.json", 'w') as outputFile:
	   json.dump(citiesData, outputFile, indent=2)
	# Save the outputs
	# Print the results
	print "-----------------------------"
	print "with %d cities, of which %d have population information" % (numberOfCities, withPopulationData)
	print "-----------------------------"
	#
	
if __name__ == '__main__':
	main()
	
	