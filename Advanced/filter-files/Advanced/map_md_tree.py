#!/usr/bin/python

# map_md_tree.py

"""Map Markdown files (.md) in a link Tree.

This is an advanced example script, expanding on `find_md_links_colors.py`

Like all the example before, this script takes one or more files on the command line.
It assumes these are all markdown files (with the `.md` extension).
And it starts to find all the markdown formatted links in them.

It then maps all these links in a tree, to visualize the relations between these files.

Files given to this script, which are not linked to, will be marked as orphaned.

----

As example, it can be executed by running the following command:  
`find . -name '*.md' | xargs python ./Advanced/filter-files/Advanced/map_md_tree.py`

This will search for all the `.md` files from the current directory,
and will find and map all the markdown links in these files.
"""

# TODO:
#
# In order to make this script work, we need to do the following:
# - from the given files, find the common ancestor in the directory path
# - Store the common directory path. (e.g. ~/Work/Project/)
# - Split up each file into:
# 	- file for python (the thing that this script can handle) (e.g. ~/Work/Project/Documentation/README.md)
#	- the directory of the file stripped from the common directory path. (e.g. Documentation/)
# 	- the name of the file without directory path (README.md)
#	- the combination of the two later to match with links later
#
# - For each link in the files, analyse whether
# 	- the link is an external link
#	- the link is a github link
#		- As later addition:
#		- the link is a github link to our current repository (git remote -v)
#		- in this case -> translate the link to a local link	
#	- the link an anchor on the same page
#	- the link is a local file
#   - the link is a local markdown file
#
# - For all the local markdown files:
#	- Split each linked markdown file into:
#		- directory path from the common directory path
#		- the name of the file without directory path
#		- the combination of the latter to match with files above


import os
import sys
import glob
import re

from colored import fg, attr


def getFilesFromArguments():
	"""Get the files provided on the command line.
	
	The files can be provided on the command line, either as one or multiple file arguments:
	
		e.g. `python script.py file1.md file2.md file3.md`
		
	or as resulted from a wildcard character syntax:
	
		e.g. `python script.py file*.md`
	"""
	files = []
	for arg in sys.argv[1:]:
		# Glob is needed for a cross platform solution
		files += glob.glob(arg)
	#
	# filter #1
	# Make sure that all elements are indeed files
	files = [f for f in files if os.path.exists(f)]
	#
	# filter #2
	# Make sure that the files are not empty
	files = [f for f in files if os.stat(f).st_size > 0]
	#
	return files

def findLinks(line):
	"""
	Find the links in the given line of markdown text.
	
	Arguments:
		line: a line of markdown text, which will be searched
	
	Returns:
		The markdown formatted links in the string provided,
		or an empty list [] if it finds nothing.
		It returns a list of tuples.
		Each tuple contains two elements:
		 - the title of the link
		 - the url of markdown file it links to
	
	Description:	
		Markdown formatted links follow this format:
		`[title of the link](url_or_markdown_file)`
	"""
	# The Regular Expression for a markdown link
	unreadable_pattern = r'\[([^\]]+)\]\(([^)]+)\)' # do not use code that looks like the cat jumped around on your keyboard
	# It would be better to do a multiline with some comments
	pattern = r'''
	  \[			# literal opening bracket
		(			# capture the link title
		  [^\]]+	# one or more character other than the closing bracket
		)			# stop the capture
	  \]			# literal closing bracket
	  \(			# literal opening parathesis
	    (			# capture the url or markdown file
		  [^)]+		# one or more characters other than the closing parathesis
		)			# stop the capture
	  \)			# literal closing parathesis
	'''
	
	return re.findall(pattern, line, re.VERBOSE)

def allLinksInFile(file):
	"""Finds all links in the given file
	
	Arguments:
		file: the file to read all links in.
		
	Returns:
		An array containing all the links in the given file. For each link, only the target url is returned."""
	# Start with an empty array
	links = []
	#
	# Go over each line in the file
	lines = file.readlines()
	for line in lines:
		# Find all markdown links in the each line
		# and go over each
		for link in findLinks(line):
			# Append the target url to the links array
			links.append(link[1])
	return links

def highlightMdFilesAndGitHubLinks(linktarget):
	"""Highlight an url-string with colors for command line printing.
	
	Arguments:
		linktarget: a (partial) url that is the target a the link.
	
	Returns:
		The highlighed string that can be printed with colors on the command line.
		
	Description:
		If the url is a local hosted markdown file, it will be highlighted in red
		If the url is a github url, it will be highlighted in aqua
		If the url is anything else, it will just be returned as is.
	"""
	if linktarget.endswith(".md"):
		return "%s%s%s%s" % (fg(1), attr('bold'), linktarget, attr(0))
	if linktarget.startswith("https://github.com/"):
		return "%s%s%s%s" % (fg(30), attr('bold'), linktarget, attr(0))
	return linktarget

def main():
	"""Opens the files deliverd to this script and prints all the links, using nice colors."""
	#
	# Get the files given as command line arguments
	commandLineFiles = getFilesFromArguments()
	#
	# Go over each file
	for file in commandLineFiles:
		# 'Open' the file and print its filename 
		with open(file, 'r') as f:
			links = allLinksInFile(f)
			# Prints either "(contains no links)" or "contains n links:" where n > 0
			nolinkstext = len(links) > 0 and " contains %d links:" % (len(links)) or " (contains no links)"
			print "%s%s:%s%s" % (attr('bold'), file, attr(0), nolinkstext)
			for link in links:
				print "\t%s" % (highlightMdFilesAndGitHubLinks(link))
				
	
if __name__ == '__main__':
	main()