#!/usr/bin/python

import os
from os.path import join, isdir

def listfiles(the_path, depth):
	for f in os.listdir(the_path):
		f_or_d = join(the_path, f)
		if isdir(f_or_d):
			print "%s contains:" % (f_or_d)
			listfiles(f_or_d, depth + 1)
		else:
			print "%s%s" % (''.join("\t" * depth), f)

def main():
	listfiles(".", 0)

if __name__ == '__main__':
	main()