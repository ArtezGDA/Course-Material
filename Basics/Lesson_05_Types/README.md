# Types

## Different types

Different types of data are represented by different data types in the computer:

### `int`

- whole (integral) numbers, can be negative,
- e.g. `7`, `9283712`, `0` or `-4`

### `float`

- 'floating' numbers, not fixed to integers, fractions
- e.g. `7.5`, `16.8333333` or `3.1415926`

### `bool`

- Boolean values `True` or `False`
- i.e. either `True` or `False`

### `string`

- A string of characters, representing a piece of text: a sentence, a word, a name, a title, etcetra.
- e.g. "Arnhem", "Jane Doe", "iPhone 7", "Go ahead, make my day punk!"

## Convert from one type to a different type

Use any of the special functions to convert one type to the other: `int()`, `float()` or `str()`

```python
float(5)
```

```python
int(10.6)
```

```python
float('2.5')
```

```python
str(25)
```

Or, in the case when you want to use the value as a bool: Just use it where python expects a bool, (e.g. with an `if`)

```python
if "hello":
    pass
```

## Strings, quotes and escaping

To define a string, use single quotes (`'...'`), double quotes (`"..."`) or triple double quotes (`"""..."""`)

```python
# single quotes
'mango carrot'
```

```python
# double quotes
"strawberry"
```

```python
# use \' to escape the single quote...
'doesn\'t'
```

```python
# ...or use double quotes instead
"doesn't"  
```

```python
# and vice versa, use single quotes to include a double quote
'"Yes," he said.'
```

Finally, use triple (triple double) quotes for strings which should include both single and double quotes or *new lines*.

```python
# triple quotes to define a multiline string
"""A multiline string
has triple quotes: 3 x "
at the beginning 
and end.
Let's try it out!
"""
```

### Special characters: newline, tab character

You can also include other special characters, but you have to **escape** them.

#### new lines: `\n`

```python
# new line: \n
s = "line one\nline two"
print s
```

outputs:

```python
line one
line two
```

#### tabs: `\t`

```python
# tab characters \t
s = "\t\tindented line"
print s
```

outputs:

```python
        indented line
```

## Format strings

Sometimes you want to *format* your strings in a special way, when the ingredients for this string are not literal but variable. In those case you can use *string formatting*. Think of string formatting as having a template with placeholders, in which you can fill in dynamic values.

```python
"Hello %s, how are you %s?" % ("Dirk", "today")
```

This construction has the following parts:

- the template: `"Hello %s, how are you %s?"`
- the placeholders: `%s` and `%s`
- the `%` character splitting up the template part and the values part and telling python we're string formatting.
- the (dynamic) values (in a tuple – defined with parenthesis): `("Dirk", "today")`

The above outputs the following:

```python
"Hello Dirk, how are you today?"
```

You can use these placeholders:

- `%s` for *String*  
- `%d` for *Integer digits*  
- `%f` for *Float*

Example:
  
```python
"To buy %d %s will cost you %f" % (3, "beers", 7.5)
```

outputs:

```python
'To buy 3 beers will cost you 7.500000'
```

Float precision

```python
"%.2f" % (7.5)
```

gives:

```python
'7.50'
```


### Formatting a bool as a string

When you want to format a boolean value (`True` or `False`) in a text, you can of course use `if` / `else`, but you can also make it a bit shorter:

```python
True and "yes" or "no"
False and "yes" or "no"
```


----
### Further reading and documentation

- [An Informal Introduction to Python](https://docs.python.org/2/tutorial/introduction.html) :
    - read [3.1.1. Numbers](https://docs.python.org/2/tutorial/introduction.html#numbers)
    - and [3.1.2. Strings](https://docs.python.org/2/tutorial/introduction.html#strings)
- [Text Formatting](https://pyformat.info) (second mention, concentrate on **old style** formatting for now)
