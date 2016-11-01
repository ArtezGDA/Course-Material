#!/usr/bin/python

import os
from os.path import join, isdir

def listfiles(the_path, depth):
	for f in os.listdir(the_path):
		f_or_d = join(the_path, f)
		if isdir(f_or_d):
			print "%s is a directory" % (f_or_d)
		else:
			print "%s" % (f)

def main():
	listfiles(".", 0)

if __name__ == '__main__':
	main()