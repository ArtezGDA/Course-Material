# Data Manipulation

### Tricks and Algorithms to manipulate `lists` and `dicts` with python

When dealing with data, often you want to perform (semi-complex) operations on the data, like *filtering*, *splitting*, *merging* or *reordering*. Python is a good tool to perform these tasks, because it is relatively easy to work with data objects in python like `lists` (*arrays* of data) or `dicts` (dictionaries: structured data with *key* -*value* pairs).

### Table of Contents: the algorithms

- [Flatten data](#flatten_data)
- [Build a filter list](#build_a_filter_list)
- [Compare two sets](#compare_two_sets)
- [Merge two sets](#merge_two_sets)

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

See the python script [`flatten.py`](#flatten_py) :

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

Filter from list of filters

##  Compare two sets

Compare two datasets. Find the missing / change

## Merge two sets

Merge two datasets. Combine into one.