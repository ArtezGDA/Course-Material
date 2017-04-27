# Scraping: Tips & Tricks

## Overview of the Scraping process

The process of scraping can be compared to the process of mine a rare ore:

*Acquire* -> *Parse* -> *Filter* -> *Organize*

1. **Acquire** - Automatic collection of huge quantites of data
2. **Parse** - Interpret the data as content. (e.g. parse the html into useful values)
3. **Filter** - Filter the information and only keep what is looked for
4. **Organize** - Collect these bits of information into a coherent set

## Related lessons (with *step by step* code examples)

Python technologies (and lessons) for scraping web sites:

### Scraping `HTML` data from websites 

In most cases the only way to get data from a website is to scrape one or more pages from that website. There are several python modules available to *get* and *parse* the `HTML` data:

- `Element Tree` (low level): see [scrape Disney's box office from Wikipedia](https://github.com/ArtezGDA/python-web-scraper)
- `BeautifulSoup`. See [getting list of cities from Wikipedia](Lesson_09_Scraping_Notes.md)
- `lxml` with *XPath*. See [Getting box-office numbers from Wikipedia](Lesson_07_Scraping_with_Xpath.md)

### Scraping data using an API

In other –more rare– cases, you are lucky and there is an `API` (Application Programming Interface) available to help you to acquire the data. In those cases, the maintainers of the website or service, already forsaw that you as a designer or developer, might one day be interested in acquiring the data. The existence of an API often also means that you're required to request a *API-key* first: a special token or password that controls who is granted access to their data.

- Use the `github` API to [scraping all commit messages](Lesson_05_Scraping_Github_API.md)

# Tips

###### Tools, Modules and other Setup that will help you

## `DOM`-elements in python

As said, there are various python modules available to read the `HTML` data in to a *DOM* (Document Object Model) **tree structure**. (The *tree structure* means that the `HTML` elements are organized according to their nested structure on the page: e.g. an `html` tag, containing a `body` tag, containing a `div` tag, with inside itself another `div` tag, containing multiple `<ul>` unordered lists, containg multiple `<li>` list items, etcetera ...).

These different python modules do roughly the same thing, but differ in their exact syntax and what you can do with them. E.g. `lxml` allows more complicated `xpath` queries than `Element Tree`:

- `Element Tree` – [Element Tree documentation](http://effbot.org/zone/element.htm)
- `Beautiful Soup` – [Beautiful Soup 4 documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- `lxml` – [lxml etree documentation](http://lxml.de/tutorial.html)

## Setup: apps and windows open:

- Textedit for notes **or** the Safari browser for following a tutorial
- Terminal window with 3 tabs for **git** / **ipython** / running the **python** script
- The browser (Chrome with *XPather*) to inspect the page that you attempt to scrape.
- Textmate / Atom for editing the actual python script.

## How to deal with big sets of data

If the data that you want to scrape is a big set of data, the whole process might become more difficult, the bigger the dataset gets. Processing all that data might consume significantly more time and might require significantly more diskspace. So you have to be more careful with what you do. But there are a few tips and tricks.

### Show progress bar in your script

If you are writing a python script to collect, process or analyze a big number of files or big number of elements in the data, the `tqdm` module might be useful to draw a progress bar as part of the Terminal output.

Example:

```python
from tqdm import tqdm

# When tree.findAll('li') returns a big list of elements,
# a lot of links need to be followed 
for elem in tqdm(tree.findAll('li')):
		# Perform some heavy work with elem
		[...]
```

- Show progress with `tqdm` ([tqdm documentation](https://github.com/tqdm/tqdm))

### Start with a single element from the set

Also it is smart to develop your scraping tool by starting with just a single result from the big list:

```python
# First just try to get the necessary data from the first element in our list
big_list_of_elements = tree.findAll('li')
first = big_list_of_elements[0]
print first.tag
print first.text
print first.attrib['href']
```

### Then attempt the scraping first with only a subset of data

And if that first elements can be scraped, parsed or analyzed correctly, continue with a small set (of e.g. the first 10 elements).

The slicing index `[:]` allows you to create a sub range of the original list:

```python
# As example, say we have this list:
li = ["amber", "beige", "cobalt", "desert", "emerald", "flamingo"]

# Get the first three elements
li[:3]
# >		['amber', 'beige', 'cobalt']

# Get a list with just the second element
li[1:2]
# > 	['beige']

# Get the last two elements:
li[-2:]
# >		['emerald', 'flamingo']
```

You can use this slicing technique to only process a subset of your big data set:

```python
# Say tree.findAll('li') returns a big list of elements
for elem in tree.findAll('li')[:2]:
		# Perform work only the first two elements
		[...]
```

## Deal with exceptions and anomalies

Unfortunately, most of the times, dealing with the exceptions and anomalies in your data set is the most of the work involved in scraping the data. 

As example, you might have data from different sources, one from New York, the other from Barcelona. Then probably the temperature data in those two sets are not immediately compatible, New York data will be in Fahrenheit, Barcelona data will be in Celcius.
An other example might be an amount of money as found on Wikipedia. Some pages might have this information as "$1278 million", some as "$1.3billion", some as "$1.278.000.000", and some might have no information at all.  
The process of converting all these pieces of data to a consistent and useful dataset is called "*normalization*". (Some examples below)

Making sure that your scraping script can cope with all these situations is –especially in datasets which are (partly) created by human input– often the most work.

## Collaborate!

Scraping data is a touch job. You can spend days just looking a (boring) data and numbers. And in this step of the process, it can still feel very far away from any visual gratifying results. Sometimes it can even feel like working in the dark. And building a scraping script means a lot of debugging and figuring out what the data is and how to work with it. At best the end result is a big `json` file, with lots of *arrays* and / or *dicts*. So you can use every help you get:

- Collaborate with your peers
- Ask around

----

# Tricks

###### Things that you might need to do while scraping

## Save into `json` file

- [json reading and writing](Advanced/json)

## Scrape a collection of `urls`

- Scrape from 1 `url`
- Scrape from a list of `url`s
- Scrape from 1 (top) url -> creates list of urls. Then scrape each and all of them
	- E.g. paging example
	- E.g. Scrape list of countries -> for each country scrape list of cities -> for each city scrape the population

## Convert and validate `json`

- Convert `csv` data to `json` with [Mr Data Converter](https://shancarter.github.io/mr-data-converter/)
- Validate a `json` file with [JSON Lint](http://jsonlint.com)

## Normalize data

*Normalization* is the process of converting all data values so they can be well compared with each other, or can be combined into one single graph. Examples:

- [normalizing population of cities](ScrapingLecture/filter_populations.py) (from the scraping of cities example)
- [normalizing the box office revenue numbers](https://github.com/ArtezGDA/python-web-scraper/blob/master/amount_normalizer.py) (from the Disney movies example)

## Flatten data

- [Flatten data](DataManipulation/README.md#flatten-data)

## Build a filter list

- [Build a filter list](DataManipulation/README.md#build-a-filter-list) – Use a list (of words) to filter a dataset

##  Compare two sets

- [Compare two datasets](DataManipulation/README.md#compare-two-sets) – Find the missing / change

## Merge two sets

- [Merge two datasets](DataManipulation/README.md#merge-two-sets) – Combine into one.
