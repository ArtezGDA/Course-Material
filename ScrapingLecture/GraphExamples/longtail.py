#!usr/bin/python

# longtail.py

import json
import plotdevice as pd

def mapValue(value, fromMin, fromMax, toMin, toMax):
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
	for country in citiesData:
		if country.has_key('cities'):
			for city in country['cities']:
				if city.has_key('population'):
					populationFigures.append(city['population'])
	print "%d cities with population" % len(populationFigures)
	maxPop = max(populationFigures)
	minPop = min(populationFigures)
	print "Largest is %d. Smallest is %d" % (maxPop, minPop)
	# Order the list ...
	populationFigures.sort(reverse=True)
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
		# Get the population
		figure = populationFigures[i]
		barHeight = mapValue(figure, minPop, maxPop, baseline, margin)
		# Draw a line
		pd.line(x, baseline, x, barHeight)
	pd.export('longtail.pdf')
		
	
if __name__ == '__main__':
	main()