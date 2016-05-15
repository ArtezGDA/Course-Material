# .json reading and writing

`JSON` stands for **J**ava**S**cript **O**bject **N**otation and has become the *lingua franca* of programming to store and exchange data.

There are two examples here:

- `writing.py`: a python script that writes (stores) data in a `.json` file and
- `reading.py`: a python script to read that `.json` file back in.

### Example: lottery numbers
The examples show how to store and load a structure of lottery numbers. (We could've used any example, but lottery numbers seems simple enough to explain the basics of using `.json` from python).

##### Dataformat
In the `.json` file lottery numbers for 12 months are stored. Each month has a `month` property, for the string of the month; a `numbers` property, for a list of 10 random numbers per month; and a `jackpot` property for the number receiving the bonus price.

The structure is like the following:

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
		'numbers:  [27, 29, 43, 51, 55, 57, 87, 91, 95, 100]
		'jackpot': 23
	},
	...
]
```

