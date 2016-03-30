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
	pBarCountries = tqdm(citiesData, leave=True, nested=True)
	for c in pBarCountries:
		country = c['country']
		if c.has_key('cities'):
			cities = c['cities']
			pBarCountries.set_description("Processing %s" % country)
			pBarCities = tqdm(cities, leave=True, nested=True)
			for city in pBarCities:
				# Open the city page
				
			# if listPage:
			# 	p = wikipedia.page(listPage, auto_suggest=False)
			# 	r = urllib.urlopen(p.url).read()
			# 	soup = BeautifulSoup(r, "html.parser")
			# 	tables = soup.findAll('table', class_="wikitable")
			# 	# create two empty cities list
			# 	# (one just for the city names, to prevent duplicates)
			# 	# (the second to store more info per city)
			# 	cities = []
			# 	cityDicts = []
			# 	possibleCityLinks = []
			# 	if len(tables) > 0:
			# 		# First the case when there are tables
			# 		#
			# 		for t in tables:
			# 			for tr in t.findAll('tr'):
			# 				allLinks = []
			# 				for th in tr.findAll('th'):
			# 					link = th.find('a')
			# 					if link:
			# 						allLinks.append(link)
			# 				for td in tr.findAll('td'):
			# 					link = td.find('a')
			# 					if link:
			# 						allLinks.append(link)
			# 				possibleCityLinks.append(allLinks)
			# 	else:
			# 		# Find all links in list items
			# 		div = soup.find('div', id="mw-content-text")
			# 		# Search all unordered lists
			# 		for ul in div.findAll('ul', recursive=False):
			# 			for link in ul.findAll('a'):
			# 				possibleCityLinks.append([link])
			# 		# Search all ordered lists
			# 		for ol in div.findAll('ol', recursive=False):
			# 			for link in ol.findAll('a'):
			# 				possibleCityLinks.append([link])
			# 	# Find first valid link
			# 	pBarCities = tqdm(possibleCityLinks, leave=True, nested=True)
			# 	for allLinks in pBarCities:
			# 		# Find first valid link in the links
			# 		for link in allLinks:
			# 			if appendLinkToCities(link, cities, cityDicts):
			# 				break
			# 	numberOfCities += len(cityDicts)
			# 	# Now, our cities list is filled with cities, but what to do with it.
			# 	#
			# 	# Let's append it to the dictionary c, we already had
			# 	c['cities'] = cityDicts
	# # Save a file, with all cities by countries
	# with open("city_populations.json", 'w') as outputFile:
	#    json.dump(citiesData, outputFile, indent=2)
	# print "Found list of %d cities" % (numberOfCities)
	

if __name__ == '__main__':
	main()