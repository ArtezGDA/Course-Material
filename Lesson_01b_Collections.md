# Collections

## Arrays (or *lists*)

##### Why

to store / remember a collection of the same type of elements

##### Example

`[8, 3, 7, 22]`  
`['apple', 'banana', 'carrot']`

##### Variable assignment

`a = [1, 2, 3, 4]`  
`screen_colors = ["red", "green", "blue"]`

##### Get 1 element

`a[2]` ... `3`  
`screen_colors[0]` ... `"red"` 

##### Set 1 element

`a[1] = 5`  
the list is now `[1, 5, 3, 4]`

##### Empty list

`[]`

##### Add one element to the list

`a.append(13)`  
the list is now `[1, 5, 3, 4, 13]`

##### Get and remove the last element from the list

`a.pop()` ... `13`  
the list is now back to `[1, 5, 3, 4]`

##### Count the number of elements

`len(a)` ... `4`

##### Concatenate lists

`[1, 2, 3] + [4, 5]`  
returns ... `[1, 2, 3, 4, 5]` 

## Dictionaries (*dicts*)

##### Why

to store / remember (named) properties of one object.  
Dictionaries are a *key - value* storage, that means for every **key**, it can store a specific **value**.  
E.g. if you want to remember properties of a player in a game: 'name', 'time played', 'level', 'high score' ...
 
##### Example

`{ 'foo': 42, 'bar': "Hello" }`

where `foo` and `bar` are keys, and `42` and `"Hello"` their values

##### Variable assignment

`d = { 'foo': 42, 'bar': "Hello" }`  
`player1 = {'name': "Dirk", 'coins': 23, 'time-played': 1.40}`

##### Get 1 element

`d['foo']` ... `42`  
`player1['name]` ... `"Dirk"` 

##### Set 1 element

`d['bar'] = "Yo, what's up?!!"`  
the dictionary is now ... `{ 'foo': 42, 'bar': "Yo, what's up?!!" }`
 
cheating the game:

`player1['coins] = 5500`  

##### Empty dict

`{}`

## Special tricks

##### For loop through list

Do something with each element from the array

```
for n in a:
	print n
```

Outputs:

```
1
5
3
4
```

Use variable names that make sense

```
palette = ["pale blue", "ocean", "sky"]
for color in palette:
	# do someting with color
	print color
```

or

```
for book in library:
	read(book)
```

##### Get all keys of a dictionary

The `keys()` function:

`d.keys()`  
returns an array of all the keys  
`['foo', 'bar']`

##### Does the list contains this?

The `in` keyword

`"red" in screen_colors` ... `True`  
`"geen kleur" in screen_colors` ... `False`

##### Does the dict has this key?

The `has_key()` function:

`d.has_key('f')` ... `False`  
`d.has_key('foo')` ... `True`  

##### Sorting

Return a sorted list:

`sorted(a)` ... `[1, 3, 4, 5]`

`a` is still `[1, 5, 3, 4]`

Modify the list to be sorted

`a.sort()`

returns nothing, but changes the list itself.  
`a` is now `[1, 3, 4, 5]`

## JSON import & export

## Advanced tricks

- inverse
- list comprehension (quick create list from other list)
	- `[x * 2 for x in range(5)]`
	- outputs: `[0, 2, 4, 6, 8]`
- list functions:
	- filter,
	- map,
	- reduce,
	- zip
- Simple reduce functions:
	- sum
	- min
	- max
	