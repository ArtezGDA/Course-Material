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

The last two examples work around comparing and merging **two** sets of data. This case is really common, e.g. say that you have one data set with cities and their populations, and an other dataset with cities and their geographical coordindates. Or you have the cast list of a movie (people who acted in this movie) and you have an other dataset with actors and their biography. In those case you will want to do at least two things:

- compare the two datasets. And find out which ones are the missing from the one, or are not in the other.
- and merge the datasets: extend / enhance all the data from the first set with the data from the second set.

The really simple example that I'll show you this code with are two sets that both have something with colors. The first datafile is a list of fruits and their colors. The second is a list of colorsnames and their `R`-`G`-`B` values. These example sets are reallty simple and small for a good reason: it will be easy to figure out the results yourself (even without programming). But of course, once you understand this technique you can apply it to more complex data sets.

We'll start with **comparing**

### Example

We have to *json* files with data: [`setA_fruits.json`](setA_fruits.json) and [`setB_colors.json`](setB_colors.json).

They look like this:

```js
[
  {"fruit": "apple", "color": "crimson"},
  {"fruit": "banana", "color": "canary"},
  {"fruit": "coconut", "color": "beige"},
// ...
]
```

So a *list of dictionaries*, where each dictionary has two *keys*: `fruit` and `color`

And

```js
[
  {"colorName": "amber", "red": 0.86, "green": 0.74, "blue": 0.14},
  {"colorName": "beige", "red": 0.83, "green": 0.92, "blue": 0.78},
  {"colorName": "crimson", "red": 0.94, "green": 0.04, "blue": 0.08},
// ...
]
```

A *list of dictionaries*, where each dictionary has four *keys*: `colorName`, `red`, `green` and `blue`.

### Code

#### Load the data

We start by reading both data files, and load the data in to two variables: `dataSetA` and `dataSetB`. 

```python
import json
#
with open('setA_fruits.json') as file1:
    dataSetA = json.load(file1)
with open('setB_colors.json') as file2:
    dataSetB = json.load(file2)
```

Let's start with a formal comparison: the number of elements in each:

```python
print len(dataSetA)
print len(dataSetB)
```

>`7`
>`6`

So you can already see there is a difference. (That might not be a problem, it could be that two fruits have the same color. But counting the elements is a good start).

#### Missing from set A

Now, we're gonna determine if every fruit in the *fruit list* (Set A) has its color in the *color list* (Set B). And if not, let's print out these fruits and their missing colors.

##### Check the existence of a color

First let's create a simpler list of only the color names from the list of colors (Set B). We going to use a simple *list comprehension* for this:

```python
listOfColorNames = [c["colorName"] for c in dataSetB]
```

If you print this new variable `listOfColorNames`, you get

>`[u'amber', u'beige', u'crimson', u'desert', u'emerald', u'fuchsia']`

In a simple list of strings like this, it is easier to look for the exitstance of an element with the `in` keyword:

```python
"amber" in listOfColorNames
```

Returns *`True`*

```python
"blue" in listOfColorNames
```

Returns *`False`*

##### Create a list of unmatched fruits

Create a list of all the fruits which color is missing from the list of colors, because **that** is what we want to know. (Is our data set complete? What are we still missing?)

Let's loop though all the fruits, and if the fruit is not in the list of colors print it out to the console:

```python
for fruit in dataSetA:
    if not fruit["color"] in listOfColorNames:
        print fruit
```

But wait: even better it would be to create a new list and fill this list with all the unmatched colors:

```python
unmatchedFruits = []
for fruit in dataSetA:
    if not fruit["color"] in listOfColorNames:
        unmatchedFruits.append(fruit)
```

Then we print the length of this list, and maybe also its content:

```python
print "Number of unmatched fruits:", len(unmatchedFruits)
print unmatchedFruits
```

Note also that if `len(unmatchedFruits)` would be `0` we know that every fruit's color would actually have matching `R`-`G`-`B` value.

In our example, this is not the case: we miss 3 colors. So we'll have to decide how to deal with that: skip these fruits, give them a default `R`-`G`-`B` value or find a data source which actually contains the missing colors. But we'll worry more about these missing colors when we're doing the *merge* ...

#### Missing from set B

Final step in our comparison, similar to finding unmatched fruits, it might be also interesting to find *unused colors*. (I.e. colors which we are defined in set B with an `R`-`G`-`B` value, but which are actually not needed, because there is no fruit with that color.)

The code is quite similar:

```python
# Use list comprehesion to create a list of just the color (names)
listOfFruitColors = [c["color"] for c in dataSetA]
# Then create an empty list and fill it with all the ununsed colors
unusedColors = []
for color in dataSetB:
    if not color["colorName"] in listOfFruitColors:
        unusedColors.append(color)
```

#### Output

Check the final script: [`compare.py`](compare.py) 

If we run that on our example files, we get the following output. Now we know which set is imcomplete and in which way:

```python
setA: 7
setB: 6
------------------------------
Number of unmatched fruits: 3
missing colors: [u'canary', u'yellow', u'green']
------------------------------
Number of unused colors: 2
unused colors: [u'amber', u'desert']
```

## Merge two sets

Now we know what the difference is between our two sets of data, we can try to merge them and combine them into one. Let's take the same example as before with [comparing two sets](#compare-two-sets) : a set of fruits (set A) and a set of colors (set B).

### Solving inconsistencies between the sets

As we seen from the result of the comparison, these two sets are not completely matching. So we need to decide what we we're going to do with the inconsistencies. Roughly speaking there are three ways of dealing with these kinds of problems (when the data sets do not line up exactly):

- **Skip the unmatched fruits**: discard and remove the fruits which colors we could not find.
- **Use a default value**: give fruits which colors cannot be determined a default value for the color, like black `(0, 0, 0)`, so we keep them in the list, and still allows us to work with them, just with a color which is not accurate.
- **Find the missing colors**: maybe these quick-fix solutions are not sufficient, and we really need to find the missing colors. In that case you need to go look for additional data and perform the comparison and merge steps again with any new data.

For today, we'll be using a default color.

```python
# Use black as the default color
defaultColor = {"red": 0.0, "green": 0.0, "blue": 0.0}
```

### Code

The basic structure of the code to *merge* the two sets is comparible to the structure of the code to *compare* the sets: you'll be loading the two sets of data into variables. Then you'll use a `for` loop to iterate over all the fruits in set A. And inside the `for` loop, you check each color to see *if this color is in the list of colors*. And when it is, –and *here* the code for merging differs from the code for comparing– you add the properties for `red`, `green` and `blue` to the this fruit. Finally you'll save the data as a new `json` file.

#### Get a specific color dict from a color name

One of the challenges is to get a *color dict* (e.g. `{"colorName": "crimson", "red": 0.94, "green": 0.04, "blue": 0.08}`) from the list of colors, from just the color name (e.g. `"crimson"`).

We do this by creating a list of just the color names (the same as we did when comparing the two sets):

```python
# Create a list of just the colornames from set B
listOfColorNames = [c["colorName"] for c in dataSetB]
```

Then, inside the `for` loop, when we know *which color* we're looking for, we first check to see if this color is in the list of color names. Then we use its index (the position in the list where that color name is kept), to look up the *dict* in the original list.

```python
for fruit in dataSetA:
    thisColorName = fruit["color"]
    if thisColorName in listOfColorNames:
        indexOfColor = listOfColorNames.index(thisColorName)
        color = dataSetB[indexOfColor]
```

##### The index of an element in a list

Before I'll continue, let's demonstrate this technique a bit further. Say the original list of colors has 4 colors: white, blue, yellow  and black:

```python
[{"colorName": "white", "rgb": "fff"}, {"colorName": "blue", "rgb": "00f"}, {"colorName": "yellow", "rgb": "ff0"}, {"colorName": "black", "rgb": "000"}]
```

Then the `listOfColorNames` (as created with the list comprehension like above) will be the following:

```python
["white", "blue", "yellow", "black"]
```

Let's say the color we're looking for is `"yellow"`. As you can see, `"yellow"` is stored at the 3rd position, with index `2`. (Remember: python starts counting with `0`).

The python code to get that number (`2`) is `.index()`

```python
listOfColorNames.index("yellow")
```

Returns *`2`*

And because `"yellow"` is stored at index `2` in the list of color names `listOfColorNames`, it is save to assume the full dict for *yellow* (`{"colorName": "yellow", "rgb": "ff0"}`) is also stored at index `2`. So if we know the index of color name in the simplified list, we know the index of the full dict in the original list:

```python
		indexOfColor = listOfColorNames.index(thisColorName)
		color = dataSetB[indexOfColor]
```

#### Using the default color for when the fruit color was not defined in the list of color

We check whether the color name is in the list of colors before we look for its index:

```python
    if thisColorName in listOfColorNames:
				# getting the color its the index
```

But if the color is not in the list of colors, we use a default color. Again, the use of a *default color* is a conscious choice. It might not be the best solution in your case. For this example it will do:

```python
    else:
        color = defaultColor
```

#### Add the *merging* properties to the fruit dict

The actual merge of the data is when we add the properties from an element from *set B*, to the corresponding element from *set A*. In our case the element we found from set B is stored in a variable the `color`. And we iterate over the elements from set A with a for loop where each element is the variable `fruit`.

So we need to add the missing / merged properties, i.e the properties that are in set B, but not in set A. Those are the properties that we want to merge from `color` into `fruit`. In our case these are the color values for `"red"`, `"green"` and `"blue"`.

```python
		# Set all the color properties which we want to merge
		fruit["red"] = color["red"]
		fruit["green"] = color["green"]
		fruit["blue"] = color["blue"]
```

Since this list of properties is quite small we're done now. But we would have more properties, we could also shorten this code by putting the keys in a list of strings, and then iterating over that list:

```python
		# List of the properties which we want to merge
		mergingProperties = ["red", "green", "blue"]
		# Add each property
		for prop in mergingProperties:
				fruit[prop] = color[prop]
```

But this will not be included in the final code. I'll leave this as an exercise for you.

### Output

If you run the final script [`merge.py`](merge.py) it creates a new file `merged_setAB.json` with content like this:

```python
[
  {
    "blue": 0.08,
    "color": "crimson",
    "fruit": "apple",
    "green": 0.04,
    "red": 0.94
  },
  {
    "blue": 0.0,
    "color": "canary",
    "fruit": "banana",
    "green": 0.0,
    "red": 0.0
  },
  {
    "blue": 0.78,
    "color": "beige",
    "fruit": "coconut",
    "green": 0.92,
    "red": 0.83
  },
  // ...
]
```

So this data is a merged set from the fruits with their color names, and the actual color values from the list of colors.
