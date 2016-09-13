# Variables

## Definition

A *variable* is a specific location in the computer memory, where we can store values. And we can give variables a name, so we can refer to them later. The concept is that we can use the same variable (identified by its name) at several moments in our code, *while its **value** might **change***.

## Simple example

This is the simplest example of a variable: to define and set it:

```python
x = 42
```

This will craete

```python
myVar = 5
otherVar = myVar
print myVar, otherVar
# later ...
myVar = 25
print myVar, otherVar
```


## `while` loop

Last time we learned how to use the for loop, but sometimes a normal for loop won't work, because you might not know in advance how many iterations it will take. Then it might be better to use a `while` loop.

As a simple example of a `while` loop, which produces the same result as our first `for` loop:

```python
i = 0
while i < 5:
	print i
	i += 1
```

These can be use cases for the while loop:

- when checking some value until it fits, metafore example: number lock with 4 digits
- when you don't know how many iterations you need
- when calculating the number of items is hard or difficult
- when you just want to find the first value, and not take too long in doing so
- special cases: `while True:` When you want something to keep running 'forever'


## Variables and scope (`global`)

Follow the `global_variables_n` examples

<!-- ## Types

## String quotes

In python you can use 3 different types of quotes:

str = 'single quote'
str = "double quote"


## Escaping characters -->


## References

For more reading material about these topics and more extensive explanations about the underlying stuff, read and study these online lessons:

- [Learn Python the hard way - While loops](https://learnpythonthehardway.org/book/ex33.html)
- [Python Course - Data Types and Variables](http://www.python-course.eu/variables.php)