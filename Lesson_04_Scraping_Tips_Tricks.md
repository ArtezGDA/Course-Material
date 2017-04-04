# Scraping: Tips & Tricks

## Overview of the Scraping process

The process of scraping can be compared to the process of mine a rare ore:

*Acquire* -> *Parse* -> *Filter* -> *Organize*

1. **Acquire** - Automatic collection of huge quantites of data
2. **Parse** - Interpret the data as content. (e.g. parse the html into useful values)
3. **Filter** - Filter the information and only keep what is looked for
4. **Organize** - Collect these bits of information into a coherent set

## Related code examples and lessons

Python technologies (and lessons) for scraping web sites:

- `Element Tree` (low level): see [scrape Disney's box office from Wikipedia](https://github.com/ArtezGDA/python-web-scraper)
- `BeautifulSoup`. See [getting list of cities from Wikipedia](Lesson_09_Scraping_Notes.md)
- Use the `github` API to [scraping all commit messages](Lesson_05_Scraping_Github_API.md)
- `lxml` with *XPath*. See [Getting box-office numbers from Wikipedia](Lesson_07_Scraping_with_Xpath.md)

# Tips

###### Tools, Modules and other Setup that will help you

## `DOM`-elements in python

- `Element Tree` – [Element Tree documentation](http://effbot.org/zone/element.htm)
- `Beautiful Soup` – [Beautiful Soup 4 documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- `lxml` – [lxml etree documentation](http://lxml.de/tutorial.html)

## Setup: apps and windows open:

- Textedit for notes
- Terminal window with 3 tabs for git / ipython / executing
- Browser
- Textmate / Atom for editing

## Show progress

- Show progress with `tqdm` ([tqdm documentation](https://github.com/tqdm/tqdm))

## Deal with exceptions and anomalies

- Deal with exceptions and anomalies

## Collaborate!

- Collaborate with your peers
- Ask around

----

# Tricks

###### Things that you might need to do while scraping

## Save into `json` file

- [json reading and writing](https://github.com/ArtezGDA/Course-Material/tree/master/Advanced/json)

## Scrape a collection of `urls`

- Scrape from 1 `url`
- Scrape from a list of `url`s
- Scrape from 1 (top) url -> creates list of urls. Then scrape each and all of them
	- E.g. paging example

## Normalize data

Examples:

- population of cities example
- box office numbers example

## Flatten data

- Flatten data (weather data example ... other)

## Build a filter list

- Filter from list of filters

##  Compare two sets

- Compare two datasets. Find the missing / change

