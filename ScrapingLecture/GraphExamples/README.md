# Graph Examples

### Demonstrating how to create some graphs from the JSON data

## Visualizing the "Long Tail"

Our data has 14072 cities with population figures. The assumption is that the population will be distributed in a long tail: a few cities have extremely high numbers of populations, while the majority of cities will have very small number of populations.

Because we have so much data (14072 cities), we need to think of a strategy to map these into a single graph.

First do some more analysis on the data.

Find out how much cities with populations there are exactly:

```
	citiesWithPopulations = []
	for country in citiesData:
		if country.has_key('cities'):
			for city in country['cities']:
				if city.has_key('population'):
					citiesWithPopulations.append(city['name'])
	print "%d cities with population" % len(populationFigures)
```

Then create a similar list of population figures, and find out which city has the least inhabitants and which has the most:

```
    populationFigures = []
        [...]
            [...]
                [...]
					populationFigures.append(city['population'])
```

```
	maxPop = max(populationFigures)
	minPop = min(populationFigures)
	indexOfMax = populationFigures.index(maxPop)
	indexOfMin = populationFigures.index(minPop)
	maxName = citiesWithPopulations[indexOfMax]
	minName = citiesWithPopulations[indexOfMin]
	print "Largest is %d (%s). Smallest is %d (%s)" % (maxPop, maxName, minPop, minName)
```

Order the list of populatiosn:

```
	populationFigures.sort(reverse=True)
```

And print some bar charts

```
	pd.size(512, 512)
	pd.background(0.8)
	pd.stroke(0.5)
	margin = 10
	# Take every 10th city
	for i in range(0, len(populationFigures), 10):
		x = mapValue(i, 0, len(populationFigures), margin, pd.WIDTH - margin)
        x1 = x
        x2 = x
		# Get and convert the population
		y1 = pd.HEIGHT - margin #baseline
	    y2 = mapValue(populationFigures[i], minPop, maxPop, baseline, margin)
		pd.line(x1, y1, x2, y2)
	pd.export('longtail.pdf')
```

![Long Tail graph](longtail.png)

## This lesson also shows how to draw the cities on a map

![worldmap.png](worldmap.png)