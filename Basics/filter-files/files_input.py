#!/usr/bin/python

# input_files.py

"""Example script that can be given one or more files on the command line.
It outputs the name of the file and the first line of the file itself.

As example, it can be executed by running the following command:  
`find . -name '*.md' | xargs python ./Basics/filter-files/files_input.py`  
(This searches for all the `.md` files from the current directory, and then send the output of these files to this script).

As a simple example, this script just prints the name of the file and the first line of content
"""

import os
import sys
import glob

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


def main():
	"""Opens the files deliverd to this script
	and print the first line.
	"""
	#
	# Get the files given as command line arguments
	commandLineFiles = getFilesFromArguments()
	#
	# Print the first line of each file
	for file in commandLineFiles:
		with open(file, 'r') as f:
			print "file %s:" % (file)
			lines = f.readlines()
			print lines[0]
	
if __name__ == '__main__':
	main()