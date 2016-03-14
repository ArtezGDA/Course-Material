#!/usr/bin/python

# regex_example.py

""" A few python examples using Regular Expressions to demonstrate filtering, finding, and search & replace
"""

import re

def pulp_fiction_scene_as_lines():
	"""Return the script of the 'What'-scene from Pulp Fiction as list of lines of text."""
	lines_of_text = [
		"I'm sorry, did I break your concentration? I didn't mean to do that. Please, continue, you were saying something about best intentions. What's the matter? Oh, you were finished! Well, allow me to retort. What does Marcellus Wallace look like?",
		"What?",
		"What country are you from?",
		"What? What? Wh - ?",
		'''"What" ain't no country I've ever heard of. They speak English in What?''',
		"What?",
		"English, motherfucker, do you speak it?",
		"Yes! Yes!",
		"Then you know what I'm sayin'!",
		"Yes!",
		"Describe what Marcellus Wallace looks like!",
		"What?",
		"Say 'what' again. Say 'what' again, I dare you, I double dare you motherfucker, say 'what' one more Goddamn time!",
		"He... he's black...",
		"Go on...",
		"He's bald",
		"Does he look like a bitch?",
		"What?",
		"DOES HE LOOK LIKE A BITCH?",
		"No!",
		"Then why you try to fuck him like a bitch?",
		"I didn't...",
		"Yes you did. Yes you did! You tried to fuck him. And Marcellus Wallace don't like to be fucked by anybody except Mrs. Wallace."
	]
	return lines_of_text

def filter_single_demo():
	"""Demonstration of how to filter a single line using a regex"""
	
	# Assume a single line corpus:
	corpus = """I'm sorry, did I break your concentration? I didn't mean to do that. Please, continue, you were saying something about best intentions. What's the matter? Oh, you were finished! Well, allow me to retort. What does Marcellus Wallace look like?"""
	
	# Find out if the text contains the word "Marcellus"
	m_found = re.search(r'Marcellus', corpus)
	print m_found
	# >>> <_sre.SRE_Match object at 0x10a02b098>
	
	# Find out if the text contains the word "bitch"
	m_not_found = re.search(r'a bitch', corpus)
	print m_not_found
	# >>> None
	
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
	
def filter_multiple_demo():
	"""Demonstration of how to filter a multiple lines using a regex"""
	
	# To filter multiple lines, let's make the corpus into a list of lines.
	# (If your corpus is a text file from outside your python script,
	# it is very easy to read all content in as a list of lines.)
	corpus = pulp_fiction_scene_as_lines()
	
	# Loop through all the lines
	for line in corpus:
		# Check if the line contains 'What' or 'what'
		if re.search(r'[Ww]hat', line):
			# Print only the lines that contain 'what' 
			print line
	# >>> I'm sorry, did I break your concentration? ... 
	# >>> What country are you from?
	# >>> What? What? Wh - ?
	# >>> "What" ain't no country I've ever heard of. They speak English in What?
	# ... (11 lines in total)

def findall_demo():
	"""Demonstration of how to find all occurances of a pattern"""
	
	# To demonstrate the find all, we're going to use one long block of text as corpus
	corpus = "\n".join(pulp_fiction_scene_as_lines())
	
	# Find all occurances of words starting with a upper case letter
	all_occurances = re.findall(r'\b[A-Z]\w*', corpus)
	print all_occurances
	# >>> ['I', 'I', 'I', 'Please', 'What', ... , 'Mrs', 'Wallace']

	# Use the finditer function and a for loop to get a list of matches
	for m in re.finditer(r'\b[Bb]\w*', corpus):
		print "at position {}, we found: {}".format(m.span(), m.group())

def search_replace_demo():
	"""Demonstration of how to use search and replace with regex"""
	
	# For the search and replace, take a smaller section of the script
	corpus = """
Describe what Marcellus Wallace looks like!
He... he's black...  
Go on...  
He's bald  
Does he look like a bitch?  
What?  
"""
	corpus = re.sub(r'\b[Bb]\w*', '\g<0>izzle', corpus)
	print corpus
	# >>> Describe what Marcellus Wallace looks like!
	# >>> He... he's blackizzle...  
	# >>> Go on...  
	# >>> He's baldizzle  
	# >>> Does he look like a bitchizzle?  
	# >>> What?  
	
def compile_regex_demo():
	"""Demonstration of how to compile a regex first, and then use the compiled regex"""

	# Use the same corpus as before
	corpus = "\n".join(pulp_fiction_scene_as_lines())
	
	# Create a compiled regular expression and keep it in a variable
	uppercase_pattern = re.compile(r'\b[A-Z]\w*')
	
	# Use the compiled regex to find all
	all_occurances = uppercase_pattern.findall(corpus)
	print all_occurances
	# Yield the same results as before but now faster
	# >>> ['I', 'I', 'I', 'Please', 'What', ... , 'Mrs', 'Wallace']
	
def main():
	"""Examples of regex to filter, find or search & replace"""
	filter_single_demo()
	print "----"
	filter_multiple_demo()
	print "----"
	findall_demo()
	print "----"
	search_replace_demo()
	print "----"
	compile_regex_demo()
	
if __name__ == '__main__':
	main()