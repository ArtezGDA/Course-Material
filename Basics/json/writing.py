#!/usr/bin/python

# writing.py

"""Example for writing a .json file.

This script creates 'random data' and stores that in a `.json` file.
The file is called `lottery.json` and contains the following like structure:

```
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

To create the random numbers, it took some code.
If you're only interested in the json file writing (or reading),
please look only in the main() function.

"""

import json

from random import randint
months = [
	"January",
	"February",
	"March",
	"April",
	"May",
	"June",
	"July",
	"August",
	"September",
	"October",
	"November",
	"December"
]
jsonfile = "lottery.json"


def main():
	# Create the list of dicts
	lotteryData = random_lottery_data()
	
	# JSON EXAMPLE BEGINS HERE
	
	with open(jsonfile, 'w') as outputFile:
		json.dump(lotteryData, outputFile)
	
	# 
	# Print statement if its done
	print("created lottery numbers for %d months" % (len(lotteryData)))
#
# Helper function to create the lottery data (in the format descrived above)

def random_lottery_data():
	"""Returns a list of dicts, with each dict being a month with random numbers"""
	lotteryMonths = []
	for month in months:
		random_dict = {}
		random_dict['month'] = month
		random_dict['numbers'] = random_numbers()
		random_dict['jackpot'] = random()
		lotteryMonths.append(random_dict)
	return lotteryMonths

#
# Helper functions to create a series of random numbers

def random():
	"""Returns a random number between 1 and 99"""
	return randint(1, 99)

def random_numbers():
	"""Returns a sorted array of random numbers.
	It makes sure no double occurances are picked.
	"""
	numbers = []
	# As long as the list is not yet 10 elements long, attempt to add a number
	while len(numbers) < 10:
		r = random()
		# Only add a number to the list, if it was new to the list
		if r not in numbers:
			numbers.append(r)
	# Return a sorted version of the list
	return sorted(numbers)

if __name__ == '__main__':
	main()