#!/usr/bin/python

# scrape_wiki_countries.py

import wikipedia
from bs4 import BeautifulSoup
import urllib
import json


def main():
	"""Does all the scraping work"""
	#
	# First scrape all the countries
	r = urllib.urlopen("https://en.wikipedia.org/wiki/Lists_of_cities_by_country").read()
	soup = BeautifulSoup(r)
	listitems = []
	# Find the flags
	flags = soup.find_all("span", class_="flagicon")
	for f in flags:
		# From each flag, get the parent
		listitems.append(f.parent)
	# Now get the countries
	citiesData = []
	for l in listitems:
		if len(l.findChildren("a")) >= 3:
			country = {}
			country['citiesList'] = l.findChildren("a")[-2]['title']
			country['country'] = l.findChildren("a")[-1]['title']
			citiesData.append(country)
	# Save an intermediate file, with all countries
	with open("countries.json", 'w') as outputFile:
	   json.dump(citiesData, outputFile)
	print "Found list of %d countries" % (len(citiesData))
	#
	# Then continue getting the cities
	numberOfCities = 0
	for c in citiesData[:8]:
		p = wikipedia.page(c['citiesList'])
		p.url
		r = urllib.urlopen(p.url).read()
		soup = BeautifulSoup(r)
		tables = soup.findAll('table', class_="wikitable")
		# create an empty cities list
		cities = []
		if len(tables) > 0:
			# First the case when there are tables
			#
			for t in tables:
				for tr in t.findAll('tr'):
					for td in tr.findAll('td'):
						link = td.find('a')
						if link and link.has_attr('title'):
							cityName = link['title']
							# remove duplicates and broken pages
							if cityName and not cityName.endswith('(page does not exist)') and not cityName in cities:
								cities.append(cityName)
								break
		
		else:
			# Find all valid links in list items
			div = soup.find('div', id="mw-content-text")
			# Search all unordered lists
			for ul in div.findAll('ul', recursive=False):
				for link in ul.findAll('a'):
					if link.has_attr('title'):
						cityName = link['title']
						# remove duplicates and broken pages
						if cityName and not cityName.endswith('(page does not exist)') and not cityName in cities:
							cities.append(cityName)
			# Search all ordered lists		  
			for ol in div.findAll('ol', recursive=False):
				for link in ol.findAll('a'):
					if link.has_attr('title'):
						cityName = link['title']
						# remove duplicates and broken pages
						if cityName and not cityName.endswith('(page does not exist)') and not cityName in cities:
							cities.append(cityName)
		numberOfCities += len(citiesData)
		# Now, our cities list is filled with cities, but what to do with it.
		#
		# Let's append it to the dictionary c, we already had
		c['cities'] = cities
	# Save a file, with all cities by countries
	with open("cities.json", 'w') as outputFile:
	   json.dump(citiesData, outputFile)
	print "Found list of %d cities" % (numberOfCities)
	
	
	

if __name__ == '__main__':
	main()