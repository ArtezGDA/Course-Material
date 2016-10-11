# Collections

Python knows two types of collections: *lists* and *dictionaries*.

- **Lists** typically store multiple elements of the same kind. Each element can be reached by its index.
- **Dictionaries** typically store all different kinds of information. Each element can be reached by its named *key*.

## Arrays (or *lists*)

### Why

To store / remember a collection of the same type of elements, e.g. a list of numbers, or a list of names.

#### Example

```python
[8, 3, 7, 22]
['apple', 'banana', 'carrot']
```

#### Variable assignment

```python
a = [1, 2, 3, 4]
screen_colors = ["red", "green", "blue"]
```

#### Get 1 element

```python
a[2]
# ... 3
```

```python
screen_colors[0]
# ... "red"
```

#### Set 1 element

```python
a[1] = 5
# the list is now [1, 5, 3, 4]
```

#### Empty list

```python
[]
```

#### Add one element to the list

```python
a.append(13)
# the list is now [1, 5, 3, 4, 13]
```

#### Get and remove the last element from the list

```python
a.pop()
# outputs ... 13
# and the list is now back to [1, 5, 3, 4]
```

#### Count the number of elements

```python
len(a)
# ... 4
```

#### Concatenate lists

```python
[1, 2, 3] + [4, 5]
# returns ... [1, 2, 3, 4, 5]
```

## Dictionaries (*dicts*)

### Why

To store / remember (named) properties of one object.  
Dictionaries are a *key - value* storage, that means for every **key**, it can store a specific **value**.  
E.g. if you want to remember properties of a player in a game: 'name', 'time played', 'level', 'high score' ...
 
#### Example

```python
{ 'foo': 42, 'bar': "Hello" }
```

where `foo` and `bar` are keys, and `42` and `"Hello"` their values

#### Variable assignment

```python
d = { 'foo': 42, 'bar': "Hello" }
player1 = {'name': "Dirk", 'coins': 23, 'time-played': 1.40}
```

#### Get 1 element

```python
d['foo']
# ... 42
player1['name']
# ... "Dirk"
```

#### Set 1 element

```python
d['bar'] = "Yo, what's up?!!"
# the dictionary is now ... { 'foo': 42, 'bar': "Yo, what's up?!!" }
```
 
cheating the game:

```python
player1['coins'] = 5500
```

#### Empty dict

```python
{}
```

----

## Special tricks

#### For loop through list

Do something with each element from the array

```python
for n in a:
	print n
```

Outputs:

```python
1
5
3
4
```

Use variable names that make sense

```python
palette = ["pale blue", "ocean", "sky"]
for color in palette:
	# do someting with color
	print color
```

or

```python
for book in library:
	read(book)
```

#### Get all keys of a dictionary

The `keys()` function:

```python
d.keys()
```

returns an array of all the keys:

```python
['foo', 'bar']
```

#### Does the list contains this?

The `in` keyword:

```python
"red" in screen_colors
# ... True
```

```python
"geen kleur" in screen_colors
# ... False
```

#### Does the dict has this key?

The `has_key()` function:

```python
d.has_key('f')
# ... False
```

```python
d.has_key('foo')
# ... True
```

#### Sorting

Return a sorted list:

```python
sorted(a)
# ... [1, 3, 4, 5]
```

`a` is still `[1, 5, 3, 4]`

Modify the list to be sorted

```python
a.sort()
# returns nothing, but changes the list itself.
```

`a` is now `[1, 3, 4, 5]`

### Advanced tricks

It's good to know about the existence of these advanced methods and operations. Because using them will clean up and simplify your code drastiscally. But these are not essential because you can write any of them from just using the building above.

- `reverse`
- list comprehension (quick create list from other list)
	- `[x * 2 for x in range(5)]`
	- outputs: `[0, 2, 4, 6, 8]`
- list functions:
	- `filter`,
	- `map`,
	- `reduce`,
	- `zip`
- Simple reduce functions:
	- `sum`
	- `min`
	- `max`