#!/usr/bin/python

# find_md_links_color.py

"""Example script, expanding on `find_md_links.py`.
As the example before, this script can be given one or more files on the command line,
and finds all the markdown formatted links in them

Additionally it colors the output.

This script is dependend on the colored module. Make sure it is installed with:  
`sudo easy_install colored`

----

Assuming the given files are all markdown (`.md`) files, the script will then search these files
for markdown formatted links (`[title of the link](url_or_markdown_file)`), and print
them to the standard out.

As example, it can be executed by running the following command:  
`find . -name '*.md' | xargs python ./Basics/filter-files/find_md_links.py`

This will search for all the `.md` files from the current directory,
and will find and print all the markdown links in these files.
"""

import os
import sys
import glob
import re

from colored import fg, attr


def getFilesFromArguments():
	"""Get the files delivered on the command line,
	either as one or multiple file arguments:
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
	"""Returns the markdown formatted links in the string provided.
	Markdown formatted links follow this format:
	`[title of the link](url_or_markdown_file)`
	
	It returns a list of tuples.
	Each tuple contains two elements:
	 - the title of the link
	 - the url of markdown file it links to
	When it doesn't find anything, it returns an empty list []
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
	"""Returns an array of all the links in the given file.
	For each link, only the target url is returned.
	"""
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

def highlightMdFiles(linktarget):
	"""Returns a string with colors for printing on the command line.
	If the url is a local hosted markdown file, it will be highlighted
	"""
	if linktarget.endswith(".md"):
		return "%s%s%s%s" % (fg(1), attr('bold'), linktarget, attr(0))
	return linktarget

def main():
	"""Opens the files deliverd to this script
	and prints all the links, using nice colors.
	"""
	#
	# Get the files given as command line arguments
	commandLineFiles = getFilesFromArguments()
	#
	# Go over each file
	for file in commandLineFiles:
		# 'Open' the file and print its filename 
		with open(file, 'r') as f:
			links = allLinksInFile(f)
			nolinkstext = len(links) == 0 and " (contains no links)" or ""
			print "links in %s%s:%s%s" % (attr('bold'), file, attr(0), nolinkstext)
			for link in links:
				print "\t%s" % (highlightMdFiles(link))
				
	
if __name__ == '__main__':
	main()