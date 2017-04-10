# Data Manipulation

### Tricks and Algorithms to manipulate `lists` and `dicts` with python

When dealing with data, often you want to perform (semi-complex) operations on the data, like *filtering*, *splitting*, *merging* or *reordering*. Python is a good tool to perform these tasks, because it is relatively easy to work with data objects in python like `lists` (*arrays* of data) or `dicts` (dictionaries: structured data with *key* -*value* pairs).

### Table of Contents: the algorithms

- [Flatten data](#flatten-data)
- [Build a filter list](#build-a-filter-list)
- [Compare two sets](#compare-two-sets)
- [Merge two sets](#merge-two-sets)

## Flatten data

Data in a `json` file can be nested. That means *arrays* can contain *dictionaries* and *dictionaries* can contain *arrays*. Often such nested structures are quite convenient to store data and keeps the stuff organized in your files. However sometimes a nested structure is not useful, and is making other processing more difficult than it should.

E.g. in the following example the visitor information is packed in dictionaries per day, which are packed in dictionaries per month, which are packed in dictionaries per year. This is not convenient. And it woudl be better to *flatten* this structure.

### Example

Basically we want to convert a nested structure to a flattend version of the same data.

#### From `nested_structure.json`

```js
{
  "years": [
    {
      "months": [
        {
          "days": [
            {
              "data": {
                "lastPage": "products", 
                "pageViews": 890, 
                "unique": 72
              }, 
              "day": 1
            }, 
            {
              "data": {
                "lastPage": "contact", 
                "pageViews": 98, 
                "unique": 66
              }, 
              "day": 2
            }, 
// [...]
            {
              "data": {
                "lastPage": "contact", 
                "pageViews": 112, 
                "unique": 73
              }, 
              "day": 31
            }
          ], 
          "month": 1
        }, 
        {
          "days": [
// [...]					
            {
              "data": {
                "lastPage": "home", 
                "pageViews": 997, 
                "unique": 32
              }, 
              "day": 31
            }
          ], 
          "month": 12
        }
      ], 
      "year": 2017
    }
  ]
}						
```

#### Convert to `flattened_data.json`

```js
[
  {
    "day": 1, 
    "lastPage": "products", 
    "month": 1, 
    "pageViews": 890, 
    "unique": 72, 
    "year": 2016
  }, 
  {
    "day": 2, 
    "lastPage": "contact", 
    "month": 1, 
    "pageViews": 98, 
    "unique": 66, 
    "year": 2016
  }, 
  {
    "day": 3, 
    "lastPage": "products", 
    "month": 1, 
    "pageViews": 729, 
    "unique": 72, 
    "year": 2016
  }, 
// [...]
  {
    "day": 31, 
    "lastPage": "home", 
    "month": 12, 
    "pageViews": 997, 
    "unique": 32, 
    "year": 2017
  }
]
```

### Code

In order to perform this change (to flatten the data), you need to write a script that *walks* every element of the data, and stores each element in a *flat list*. In our case the data is nested in a `years` *list*, of which **each year** element contains a `months` *list*, of which **each month** element contains a `days` *list* , of which each **day element** contains a `data` *dict*, which contains the actual vistors data: `pageViews`, `unique` and `lastPage`.

The following code shows how to loop through all that data, by using **three** *nested* `for` loops:

- the outer for *years*,
- the middle of *months*
- and the inner for *days*:

Inside the innermost for loop, we take that `data` *dict*, and add the *date* properties to it: the `year`, `month` and `day`.

See the python script [`flatten.py`](flatten.py) :

```python
    # Create an empty list to store the data in
    flattened = []
    
    # Loop over each year
    for yearData in nestedData['years']:
        year = yearData['year']
        # Loop over each month
        for monthData in yearData['months']:
            month = monthData['month']
            # Loop over each day
            for dayData in monthData['days']:
                day = dayData['day']
                # Get the data
                data = dayData['data']
                # Add date (year, month and day) information to the data
                data['year'] = year
                data['month'] = month
                data['day'] = day
                # Add the data object to the flat list
                flattened.append(data)
```

The rest of the script is just reading the original file  `nested_structure.json` as python data, and finally storing the created `flattened` list as a new json file called `flattened_data.json`.

## Build a filter list

Another common task when working with data is to filter it. The example I'll be showing you is taking a *list* of *dicts* and is filtering out all the dicts of which a (named) *value* is part of a list of filtered *strings* (words). In this case the source material contains *strings* and the filter is a *list of strings*, but this technique can also be applied to other *types*.

Let's say we have a list of word freqencies from a particular corpus. (A list of word frequencies mean a list of all the words that appear in *Moby Dick* and a count *how often* they appear.) In this case our corpus is the book "*Moby Dick*" by *Melville*.

Also for convenience we've already filtered out common english words. Finally, just for this example I've limited the list to words that occur 100 times or more.

Have a look at the [counting word frequencies](../Advanced/count_word_frequency/README.md) example elsewhere in this repository, to see the complete word frequency list and how to count this from a given text file.

#### Part of source file,`word_freq.json`:

```js
[
  {"freq": 1150, "word": "whale"},
  {"freq": 639, "word": "like"},
  {"freq": 525, "word": "man"},
  {"freq": 511, "word": "ahab"},
  {"freq": 509, "word": "ship"},
  {"freq": 468, "word": "ye"},
  {"freq": 446, "word": "old"},
  {"freq": 437, "word": "sea"},
  {"freq": 337, "word": "head"},
  {"freq": 332, "word": "time"},
  {"freq": 331, "word": "boat"},
  {"freq": 330, "word": "long"},
  {"freq": 327, "word": "captain"},
// [...]
]
```

#### List of filter words

As you can see and image from *Moby Dick* a lot of words have to do with the maritime business. Words like "ship", "sea", "boat" and "captain". Let's make a list of all these words, because maybe we don't want to include these maritime words in the frequency list – or the other way around: maybe we are only interested in the martime words. I'll show code for both. But in both cases we first need the list of words that we want to filter:

```python
filterwords = [
	"boat",
	"boats",
	"captain",
	"crew",
	"deck",
	"fish",
	"fishermen",
	"lifevest",
	"mast",
	"sail",
	"sailing",
	"sea",
	"ship",
	"water",
	"whaling"
]
```

#### Code to use the filter to *exclude*

If we want to filter out the words from the list, what we need to do is: make a new list and only add those frequencies that are not in the filter list. The core are **two nested `for` loops**, *the outer* looping all the words in the frequency list, *the inner* looping over all the words to be filtered. Like this:

```python
    # Create a new list
    filteredList = []
    
    # Loop over all the entries
    for freqword in freqlist:
        # Loop over all the words in the filter
        # We use a boolean `includedInFilter` to keep track of an occasional match
        # and allow this info to be used to determine if the element should be included in the next query.
        includedInFilter = False
        for filterword in filterwords:
            # Check if the frequency word is for one of the words from the filter
            if freqword['word'] == filterword:
                includedInFilter = True
        # If the frequency word is not part of any filter, add it
        if not includedInFilter:
            filteredList.append(freqword)
```

Look at [`filter_exclude.py`](filter_exclude.py) for the whole code.

#### Code to use the filter to *include*

If we want to do the reverse: only include word frequencies that are also present in the filter list, the only thing is to change is to remove the **not**, so change the last `if not` to an `if`.

```python
        # If the frequency word is in fact part included in the filter, add it
        if includedInFilter:
            filteredList.append(freqword)
```

You can run this include filter yourself by changing just line `47` in [`filter_exclude.py`](filter_exclude.py). (Remove the `not` in that line.)

#### Results

And there you have the two filtered results:

- the frequency list, where are martime words are removed: [`excl_freq.json`](excl_freq.json)
- a much shorter frequency list, this time with only the martime words: [`incl_freq.json`](incl_freq.json)

##  Compare two sets

Compare two datasets. Find the missing / change

## Merge two sets

Merge two datasets. Combine into one.