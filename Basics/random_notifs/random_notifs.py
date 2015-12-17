#!/usr/bin/python

# random_notifs.py

import json
import random

def randomLine():
	jsonfile = "sentences.json"
	with open(jsonfile) as data_file:
		data = json.load(data_file)

	# print len(data)
	return random.choice(data)

def main():
	print randomLine()

if __name__ == '__main__':
	main()