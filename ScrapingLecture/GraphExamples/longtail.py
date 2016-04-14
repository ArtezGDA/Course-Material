#!usr/bin/python

# longtail.py

import json
import plotdevice as pd

def mapValue(value, fromMin, fromMax, toMin, toMax):
	"""Function to convert the value from the 'fromRange' to the 'toRange'"""
	# Figure out how 'wide' each range is
	fromSpan = fromMax - fromMin
	toSpan = toMax - toMin
	
	# Convert the from range into a 0-1 range (float)
	valueScaled = float(value - fromMin) / float(fromSpan)
	
	# Convert the 0-1 range into a value in the to range.
	return toMin + (valueScaled * toSpan)


def main():
	"""docstring for main"""
	with open("population_of_cities.json", 'r') as inputFile:
		citiesData = json.load(inputFile)
	#
	populationFigures = []
	citiesWithPopulations = []
	for country in citiesData:
		if country.has_key('cities'):
			for city in country['cities']:
				if city.has_key('population'):
					populationFigures.append(city['population'])
					citiesWithPopulations.append(city['name'])
	print "%d cities with population" % len(populationFigures)
	# Analyze the smallest and biggest cities
	maxPop = max(populationFigures)
	minPop = min(populationFigures)
	indexOfMax = populationFigures.index(maxPop)
	indexOfMin = populationFigures.index(minPop)
	maxName = citiesWithPopulations[indexOfMax]
	minName = citiesWithPopulations[indexOfMin]
	print "Largest is %d (%s). Smallest is %d (%s)" % (maxPop, maxName, minPop, minName)
	#
	# Order the list ...
	populationFigures.sort(reverse=True)
	#
	# Draw some pdf using plotdevice
	pd.size(512, 512)
	pd.background(0.8)
	pd.stroke(0.5)
	margin = 10
	# Take every 10th city
	for i in range(0, len(populationFigures), 10):
		# Calculate the x
		x = mapValue(i, 0, len(populationFigures), margin, pd.WIDTH - margin)
		baseline = pd.HEIGHT - margin
		# Get and convert the population
		figure = populationFigures[i]
		barHeight = mapValue(figure, minPop, maxPop, baseline, margin)
		# Draw a line
		pd.line(x, baseline, x, barHeight)
	pd.export('longtail.pdf')
		
	
if __name__ == '__main__':
	main()