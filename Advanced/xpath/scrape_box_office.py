#!/usr/bin/env python

'''
This script will get all the titles and links from all the Disney movies,
and then use these links to further scrape data: the box-office revenues
'''

from lxml import etree
import requests

# The main url as starting point
url = "https://en.wikipedia.org/wiki/List_of_Walt_Disney_Animation_Studios_films"

# Get the request, html and make the tree
r = requests.get(url)
html = r.text
tree = etree.HTML(html)

# Use xpath to scrape a list of titles and links
li = tree.xpath('//span[@id="Released"]/following::table[1]//td[@class="summary"]//a')

# Loop over each title
for elem in li:
    link = "https://en.wikipedia.org" + elem.attrib['href']
    # Get the subpage and its tree
    req = requests.get(link)
    h = req.text
    t = etree.HTML(h)
    # Scrape the box office of this subpage
    box_office = t.xpath("//th[text()[contains(.,'Box office')]]/following::td[1]")
    # And print its text contents (only if there are actually box office numbers)
    if len(box_office) > 0:
        print box_office[0].text
    