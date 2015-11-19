#!/usr/bin/python

# read_from_prefered.py

"""Example scripts to read input from one of two possible sources:
from the standard input (stdin) or if the stdin is empty,
from the arguments given on the command line.

This script also logs to an external logfile.
(the example.log file in the same directory).
It is useful to log to a file, so you can inspect the process of your coding.

And in this script you probably don't want to print to the standard out (stdout),
because you want to use the stdout for an other output: the main output of the script. 
"""

import sys
import logging

def setup():
	# Setup logging
	logging.basicConfig(filename='example.log',level=logging.DEBUG)

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
	setup()
	#
	# Read from prefered input
	text_in = readFromPrefered()
	#
	# Log to the console
	logging.debug("input has %d characters:" % (len(text_in)))
	# 
	# Print to the output
	print text_in
	
if __name__ == '__main__':
	main()