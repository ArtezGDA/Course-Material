# Text in python

## Strings in python

##### Simple string:

`a = "Simple string"`  
`b = 'or with single quotes'`

##### Comment:

`# this is a comment`

##### Multiline comment:

```
# 1 this
# 2 is
# 3 a
# 4 multiple
```

##### String with a quote

`c = "Mario's pizza"`  
`d = 'she says: "Hi"'`  

##### String with single and double quotes

`e = """Within triple quotes you'll do "anything". """`

##### DocString

```
def myFunc():
	"""Here we can explain what myFunc does"""
	pass
```
usage:

```
myFunc.func_doc
# or
help(myFunc)
```

##### String concatenation

`"Hello " + "World"`  
becomes  
`'Hello World'`

##### String Formatting

`"Hello %s, how are you %s?" % ("Dirk", "today")`  
outputs  
`"Hello Dirk, how are you today?"`

`%s` for *String*  
`%d` for *Integer digits*  
`%f` for *Float*

Example:  
`"To buy %d %s will cost you %f" % (3, "beers", 7.5)`  
outputs:  
`'To buy 3 beers will cost you 7.500000'`

Float precision  
`"%.2f" % (7.5)`  
gives:  
`'7.50'`
