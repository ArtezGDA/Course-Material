#!/usr/bin/python

# run_continuesly.py

"""Run Continuesly Example

Demonstrates how to make a script run forever:
`while True:`

And demonstrates how to perform some task every 5 seconds.
Actually, because we have the script running continuesly,
in its run loop, we make it sleep 5 seconds:
`time.sleep(5)`

This results in the script performing the rest of the run loop every 5 seconds.
```
	print counter
	counter = counter + 1
```		
"""

import time

def main():
	counter = 0
	while True:
		print counter
		counter = counter + 1
		time.sleep(5)

if __name__ == '__main__':
	main()