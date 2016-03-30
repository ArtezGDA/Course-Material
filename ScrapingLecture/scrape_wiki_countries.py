#!/usr/bin/python

# scrape_wiki_countries.py

import wikipedia
from bs4 import BeautifulSoup
import urllib
import json
from tqdm import tqdm

def main():
	"""Scrapes countries from wikipedia"""
	#
	# First scrape all the countries
	r = urllib.urlopen("https://en.wikipedia.org/wiki/Lists_of_cities_by_country").read()
	soup = BeautifulSoup(r, "html.parser")
	listitems = []
	# Find the flags
	flags = soup.find_all("span", class_="flagicon")
	for f in flags:
		# From each flag, get the parent
		listitems.append(f.parent)
	# Now get the countries
	citiesData = []
	for l in tqdm(listitems):
		if len(l.findChildren("a")) >= 3:
			country = {}
			countryName = l.findChildren("a")[-1]['title']
			listPage = l.findChildren("a")[-2]['title']
			country['country'] = countryName
			# citiesList must be a exiting link and not the same as the country itself
			if not listPage.endswith('(page does not exist)') and not listPage == countryName:
				country['citiesList'] = listPage
			else:
				country['citiesList'] = ""
			citiesData.append(country)
	# Save an intermediate file, with all countries
	with open("countries.json", 'w') as outputFile:
	   json.dump(citiesData, outputFile, indent=2)
	print "Found list of %d countries" % (len(citiesData))

if __name__ == '__main__':
	main()