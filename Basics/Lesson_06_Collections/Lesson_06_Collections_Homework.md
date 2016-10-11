# Coding homework with Collections

## Lists

#### Reverse

Take the following list:

```python
pioneers = ["Bret Victor", "Ted Nelson", "Alan Kay", "Doug Engelbart", "Ivan Sutherland", "Vannevar Bush"]
```

Create a list of our pioneers in the historic correct order, i.e. reverse the order of the list. For this excersice you're not allowed to use the `reverse` function. Instead you have to write a little program using a combination of these techniques:

- a `for`-loop or
- a `while`-loop
- `pop`
- `append`

(You don't necessary have to use all of them)

Before you start programming think of an ordered deck of cards and how you would build a machine that reverses the stack of cards. This will help you figuring out this assignment.

#### Max

Take the following list:

```python
grades = [6, 5.25, 7.5, 6.25, 7, 6, 8.5, 4.0, 5.5, 6.75, 8.0]
```

Write a program that finds the biggest number in this list. For this excersice you're not allowed to use the `max` function. Use:

- a `for`-loop 
- an `if` statement

Hint: use a variable to hold the biggest number. If you encounter a number that is bigger, then replace the value of the variable with this new number.

Again, it helps visualize this problem by using a deck of cards.

## Dictionary

### Earliest invention

Once you figured out how to write the max program with numbers, you can proceed to the following assignment:

Take the following *list of dictionaries*:

```python
inventions = [
	{'author': "Bret Victor", 'invention': "Seeing space", 'year': 2013},
	{'author': "Doug Engelbart", 'invention': "Online System", 'year': 1968},
	{'author': "Vannevar Bush", 'invention': "Memex Machine", 'year': 1945}
	{'author': "Ted Nelson", 'invention': "Hypertext", 'year': 1976},
	{'author': "Ivan Sutherland", 'invention': "Sketchpad", 'year': 1963},
	{'author': "Alan Kay", 'invention': "Dynabook", 'year': 1980},
]
```

#### Assignment:

Find the *earliest* invention from this list and print the result in the following format:

> The `<WHAT>` was invented by `<WHO>` in `<WHEN>`.
