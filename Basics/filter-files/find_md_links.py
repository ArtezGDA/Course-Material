#!/usr/bin/python

# find_md_links.py

"""Example script, expanding on `files_input.py`.
As the example before, this script can be given one or more files on the command line.

Assuming these are all markdown (`.md`) files, the script will then search these files
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

def linksInLine(line):
	"""Returns the markdown formatted links in the string provided.
	Markdown formatted links follow this format:
	`[title of the link](url_or_markdown_file)`
	"""
	# The Regular Expression for a markdown link
	pattern = r'\[(.*)\]\((.*)\)'
	return []

def main():
	"""Opens the files deliverd to this script
	and print the first line.
	"""
	#
	# Get the files given as command line arguments
	commandLineFiles = getFilesFromArguments()
	#
	# Go over each file
	for file in commandLineFiles:
		# 'Open' the file and print its filename 
		with open(file, 'r') as f:
			print "links in %s:" % (file)
			# Go over each line in the file
			lines = f.readlines()
			for line in lines:
				# Find all markdown links in the each line
				linksInLine(line)
				
	
if __name__ == '__main__':
	main()