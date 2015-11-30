#!/usr/bin/python

# read_from_prefered.py

"""Example script to read input from one of two possible sources:
from the standard input (stdin) or if the stdin is empty,
from the arguments given on the command line.
"""

import sys

def readFromStdin():
	"""Reads from the standard input"""
	text_in = sys.stdin.read()
	return text_in

def hasStdin():
	"""returns whether or not the stdin has input.
	Returns false if the stdin is a stream.
	"""
	return not sys.stdin.isatty()

def readFromArguments():
	"""Reads from the arguments given"""
	# Concatenate all command line arguments into a long string
	arguments_in = sys.argv
	args_in = " ".join(arguments_in[1:])
	return args_in

def readFromPrefered():
	# Read from the stdin
	if hasStdin():
		return readFromStdin()
	else:
		return readFromArguments()

def main():
	"""Reads from the standard in or from arguments"""
	# Read from prefered input
	text_in = readFromPrefered()
	#
	# Print the number of characters and complete input
	print "input has %d characters:" % (len(text_in))
	print text_in
	
if __name__ == '__main__':
	main()