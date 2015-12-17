#!/usr/bin/python

# random_notifs.py

import json
import random
import subprocess

def randomLine():
	jsonfile = "sentences.json"
	with open(jsonfile) as data_file:
		data = json.load(data_file)

	# print len(data)
	return random.choice(data)

def executeShell(notif_string, notif_title):
	applescript = 'display notification "%s" with title "%s"' % (notif_string, notif_title)
	subprocess.call(["osascript", "-e", applescript])

def main():
	random_name = randomLine()
	executeShell("was here", random_name)

if __name__ == '__main__':
	main()