#!/usr/bin/python

# run_continuesly.py

import time

def main():
	counter = 0
	while True:
		print counter
		counter = counter + 1
		time.sleep(5)

if __name__ == '__main__':
	main()