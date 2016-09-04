# Regular Expressions in python

Regular expressions in python can be used form the buildin `re` module:

```python
import re
```

A couple of useful things you can do with regular expressions is to:
 - *filter*: find out **if** a pattern is found. Use the `search` function.
 - *find*: find the occurance(s) of a pattern. Use the `findall` function.
 - *search & replace*: find the occurances of a pattern and change those. Use the `sub` function
 
The following sections will demonstrate how to perform each of those tasks.
 
The rest of this article assumes you have a basic understanding of what Regular Expressions are, how to contruct them and when to use them. If not, first study [Lesson 08 Regex](../../Lesson_08_Regex.md)

As an example I will use this corpus to search in:  
> I'm sorry, did I break your concentration? I didn't mean to do that. Please, continue, you were saying something about best intentions. What's the matter? Oh, you were finished! Well, allow me to retort. What does Marcellus Wallace look like?  
What?  
What country are you from?  
What? What? Wh - ?  
"What" ain't no country I've ever heard of. They speak English in What?  
What?  
English, motherfucker, do you speak it?  
Yes! Yes!  
Then you know what I'm sayin'!  
Yes!  
Describe what Marcellus Wallace looks like!  
What?  
Say 'what' again. Say 'what' again, I dare you, I double dare you motherfucker, say what one more Goddamn time!  
He... he's black...  
Go on...  
He's bald  
Does he look like a bitch?  
What?  
DOES HE LOOK LIKE A BITCH?  
No!  
Then why you try to fuck him like a bitch?  
I didn't...  
Yes you did. Yes you did! You tried to fuck him. And Marcellus Wallace don't like to be fucked by anybody except Mrs. Wallace.  
  
----

### Filter

To find out *if* a pattern occurs in a given text (or series of texts), use the `search` function. It will return a `Match` object, or not.

```python
# Assume a single line corpus:
corpus = """I'm sorry, did I break your concentration? I didn't mean to do that.
Please, continue, you were saying something about best intentions. What's the matter?
Oh, you were finished! Well, allow me to retort. What does Marcellus Wallace look like?"""

# Find out if the text contains the word "Marcellus"
m_found = re.search(r'Marcellus', corpus)
print m_found
# >>> <_sre.SRE_Match object at 0x10a02b098>
```

If the regex is found in the corpus, `search` will return a `Match` object.

```python
# Find out if the text contains the word "bitch"
m_not_found = re.search(r'bitch', corpus)
print m_not_found
# >>> None
```

If it is not found, it will return `None`

The `Match` object can also be used to find out a bit more about exactly where the pattern was found. (Or more precisely, where the pattern was **first** found. Possible subsequent matches are ignored.)  
For example, use the `.group()` function to get the string of the match. (Useful if the regex could be matching multiple things).  
Or use the `.span()` function to get the position of the start and end of the match in the original string.

```python
# Respond differently depending on whether it is found or not
m = re.search(r'W.ll.c.', corpus)
if m:
	# If there is a Match, find out more about it
	print "found: {}".format(m.group())
	# >>> found: Wallace
	print "where in original: {}".format(m.span())
	# >>> where in original: (224, 231)
else:
	print "not found"
```

### Filter multiple lines

Now let's filter multiple lines of text. Let's say we have a longer document, with multiple lines, and want to filter out only the lines that contain a certain pattern. Let's filter the corpus for only the lines that contain the text 'what'.

```python
# To filter multiple lines, let's make the corpus into a list of lines.
corpus = [
	"I'm sorry, did I break your concentration? ... What does Marcellus Wallace look like?",
	"What?",
	"What country are you from?",
	"What? What? Wh - ?",
	...
]
``` 

(If your corpus is a text file from outside your python script, it is very easy to read all content in as a list of lines.)

```python
	# Loop through all the lines
	for line in corpus:
		# Check if the line contains 'What' or 'what'
		if re.search(r'[Ww]hat', line):
			# Print only the lines that contain 'what' 
			print line
```

The result is 11 lines printed out that contain 'what':

```
I'm sorry, did I break your concentration? I didn't mean to ... 
What?
What country are you from?
What? What? Wh - ?
"What" ain't no country I've ever heard of. They speak English in What?
... (11 lines in total)
```

### Find

To find all the occurances of a given pattern and receive them as a list, use the `findall` function.

```python
# To demonstrate the find all, let's make the corpus one long block of text
corpus = "\n".join(lines)
# corpus = """I'm sorry, did I break your concentration? ... """
```

Now let's try to find all the words that start with a capital (upper case) letter.

```python
# Find all occurances of a pattern
all_occurances = re.findall(r'[A-Z]\w*', corpus)
print all_occurances
```

Results in:

```json
['I', 'I', 'I', 'Please', 'What', 'Oh', 'Well', 'What', 'Marcellus', 'Wallace', 'What', 'What', 'What', 'What', 'Wh', 'What', 'I', 'They', 'English', 'What', 'What', 'English', 'Yes', 'Yes', 'Then', 'I', 'Yes', 'Describe', 'Marcellus', 'Wallace', 'What', 'Say', 'Say', 'I', 'I', 'Goddamn', 'He', 'Go', 'He', 'Does', 'What', 'DOES', 'HE', 'LOOK', 'LIKE', 'A', 'BITCH', 'No', 'Then', 'I', 'Yes', 'Yes', 'You', 'And', 'Marcellus', 'Wallace', 'Mrs', 'Wallace']
```

If you want to get a list of `Match` objects for all occurances of a pattern, use the `finditer` function and a for loop:

```python
	# Use the finditer function and a for loop to get a list of matches
	for m in re.finditer(r'\b[Bb]\w*', corpus):
		print "at position {}, we found: {}".format(m.span(), m.group())
```

Prints something like:

```
at position (119, 123), we found: best
at position (634, 639), we found: black
at position (657, 661), we found: bald
...
```

### Search & Replace

To find the occurances of a given pattern and to change each of those, use the `sub` function.

Now let's tale this one step further: let's search and replace all occurances of a word starting with a `b`, and *Snoop Dogg* forshizzle it.

```python
# For the search and replace, take a smaller section of the script
corpus = """Describe what Marcellus Wallace looks like!
He... he's black...  
Go on...  
He's bald  
Does he look like a bitch?  
What?  
"""

corpus = re.sub(r'\b[Bb]\w*', '\g<0>izzle', corpus)
print corpus
```

Now corpus has become something like:

```
Describe what Marcellus Wallace looks like!
He... he's blackizzle...  
Go on...  
He's baldizzle  
Does he look like a bitchizzle?  
What?  
```

### Pro Tip: compile the regex first

If you're using the same regex pattern multiple times in your code, it is advisable to "*compile*" the regex first. Compiling means that it will create compact computer code, which will be able to run faster. If you do not compile the regex, python will have to perform more operations, everytime you as it to `search`, `findall`, or `sub`. Compiling itself will also consume computing time. But if you are re-using the same pattern, compiled regexes will effectively run much faster.

```python
# Use the same corpus as before
corpus = "\n".join(pulp_fiction_scene_as_lines())
	
# Create a compiled regular expression and keep it in a variable
uppercase_pattern = re.compile(r'\b[A-Z]\w*')

# Use the compiled regex to find all
all_occurances = uppercase_pattern.findall(corpus)
print all_occurances
# Yield the same results as before but now faster
# >>> ['I', 'I', 'I', 'Please', 'What', ... , 'Mrs', 'Wallace']
```
