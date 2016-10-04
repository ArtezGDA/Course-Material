# Text in python

## Strings in python

##### Simple string:

```python
a = "Simple string"
b = 'or with single quotes'
```

##### Comment:

```python
# this is a comment
```

##### Multiline comment:

```python
# 1 this
# 2 is
# 3 a
# 4 multiline
# 5 comment
```

##### String with a quote

```python
c = "Mario's pizza"
d = 'she says: "Hi"'  
```

##### String with single and double quotes

```python
e = """Within triple quotes you'll do "anything". """
```

##### DocString

```python
def myFunc():
	"""Here we can explain what myFunc does"""
	pass
```
usage:

```python
myFunc.func_doc
# or
help(myFunc)
```

The `help()` tool will open a special help screen, where you can read all about the topic. As example, try the following with the previously installed *noise* library.

```python
import noise
help(noise)
```

**Note:** to exit the `help()` screen, press the **Q** key.


##### String concatenation

```python
"Hello " + "World"
```

becomes

```python
'Hello World'
```

##### String Formatting

```python
"Hello %s, how are you %s?" % ("Dirk", "today")
```

outputs  

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


##### Count chacters

```python
len("abacadabra hocus pocus")
```

returns

```python
22
```

#### More advanced stuff you could do with strings

- convert a number to a string
- convert a string into a number (if applicable)
- make lowercase / UPPERCASE / Capitalize Each Word
- count the number of occurances of a substring (or single character)
- split string into (an array) of words
- strip off characters from the beginning or end (e.g. whitespace)
- ...