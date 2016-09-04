#!/usr/bin/python

# read_from_sources.py

"""Example script to read input from different sources

This script demonstrates how to read from different inputs:

- from the standard input (stdin)
- from the arguments given on the command line
- from an interactive prompt

To make this script work and actually read from one of these sources,
uncomment the specific line in the main() function
"""

import sys

def readFromStdin():
	"""Reads from the standard input"""
	text_in = sys.stdin.read()
	return text_in

def readFromArguments():
	"""Reads from the arguments given"""
	# Concatenate all command line arguments into a long string
	arguments_in = sys.argv
	args_in = " ".join(arguments_in[1:])
	return args_in

def readFromInteractiveInput():
	"""Prompts the user for some input"""
	# Example of prompting the user for a specific input
	print "Hi, this is the interactive mode."
	typed_in = raw_input("What is your name? ")
	print "Hello %s, thanks for your input!" % (typed_in)
	return typed_in

def main():
	"""Multiple possible ways to read inputs"""
	# Uncomment one of the following lines to read
	# from the prefered input:
	# 
	# text_in = readFromInteractiveInput()
	# text_in = readFromStdin()
	# text_in = readFromArguments()
	#
	# Print the number of characters and the complete output
	print "input has %d characters:" % (len(text_in))
	print text_in
	
if __name__ == '__main__':
	main()