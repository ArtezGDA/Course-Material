#!/usr/bin/python

# random_notifs.py

"""Random Notification Display Example

Randomly pick a name and use that to dispay a notification
"""


import json
import random
import subprocess

def randomLine():
	"""Read a json file and picks a random element from a list.
	
	Assumes the root of the json file is an array of strings.
	
	Returns:
		a random string
	"""
	# The json file name
	jsonfile = "sentences.json"
	# Read the json in as data
	with open(jsonfile) as data_file:
		data = json.load(data_file)
	# return a random element from the list
	return random.choice(data)

def executeShell(notif_string, notif_title):
	"""Display a notification, using the OS X system notifications.
	
	Args:
		notif_string (str):		the notification message
		notif_title (str):		the title of the notification
	"""
	# Construct an Applescript to display the notification
	applescript = 'display notification "%s" with title "%s"' % (notif_string, notif_title)
	# Execute the Applescript from a terminal command
	subprocess.call(["osascript", "-e", applescript])

def main():
	random_name = randomLine()
	executeShell("was here", random_name)

if __name__ == '__main__':
	main()