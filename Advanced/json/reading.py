#!/usr/bin/python

# writing.py

"""Example for reading a .json file.

This script reads a 'random data' `.json` file and prints the contents.
The file, called `lottery.json` is assumed to contain the following structure:

```json
[
	{
		'month': "January",
		'numbers: [1, 17, 26, 34, 42, 48, 60, 64, 67, 90]
		'jackpot': 15
	},
	{
		'month': "February",
		'numbers:  [5, 19, 23, 66, 72, 73, 74, 75, 88, 99]
		'jackpot': 97
	},
	{
		'month': "March",
		'numbers:  [27, 29, 43, 51, 55, 57, 87, 91, 95, 98]
		'jackpot': 23
	},
	...
]
```

"""

import json

jsonfile = "lottery.json"

def main():
	"""Read the json from a file"""
	# Open the json file and read its contents
	with open(jsonfile) as data_file:
		data = json.load(data_file)
	
	# Prety print the lottery numbers
	pretty_print_lottery(data)

def pretty_print_lottery(lottery_data):
	for lottery in lottery_data:
		print "Lottery data for %s:" % (lottery['month'])
		arrayOfNumbers = lottery['numbers']
		total = sum(arrayOfNumbers)
		print "\tthis month we drew %d numbers (with a total of %d):" % (len(arrayOfNumbers), total)
		for number in arrayOfNumbers:
			print"\t\t%d" % (number)
		print "\tAnd the lucky number is: %d" % (lottery['jackpot'])

if __name__ == '__main__':
	main()