# Maping Value Math

### A few mathematical functions in python to convert values

Often when you work with values and code, you get variables, and you don't know exactly what they are. You know in what range you would like them to be. Then you need to convert them from one range to another. Or make sure they never exceed the desired range. These 4 simple functions will help you with that.

## Clip to range with `min` & `max`

If you want your values in a specific range, and do not allow them to exceed that range, you need to clip them to that range.

[graph]

To ensure that a certain value is never exceeding a given value, you can use the `max` function.

### `max(...)`

When the python `max()` value is given a list, it will return the largest value from that list

```python
max( [4, 2, 3, 0.5, 11] )
> 11
```

Or you when you just give it two values, it will pick the largest of the two:

```python
max(10, 25)
> 25 
```

So if you want to clip a random value to be **at least** a certain value, you can use the `max()` function:

```python
    # clip a value to the lower bounds (0)
    #
    oldValue = 3
    max(0, oldValue)
    # result -> 3
    #
    oldValue = -4
    max(0, oldValue)
    # result -> 0
    #
    oldValue = 35
    max(0, oldValue)
    # result -> 35
```

### `min(...)`

The same applies to the `min()` function. It will return the smallest value from a python list or list of arguments.

```python
min( [4, 2, 3, 0.5, 11] )
> 0.5
```

Or you when you just give it two values:

```python
min(10, 25)
> 10 
```

Again, you can use the function to clip values. If you want to clip a value to be **not more than** a certain value, you can use `min()`:

```python
    # clip a value to the upper bounds (10)
    #
    oldValue = 3
    min(10, oldValue)
    # result -> 3
    #
    oldValue = -4
    min(10, oldValue)
    # result -> -4
    #
    oldValue = 35
    min(10, oldValue)
    # result -> 10
```

### Combine `min` and `max`

So you can combine these two function to keep (and clip) your values between an upper and lower bounds. `Max` with the **lower** bounds. `Min` with the **upper** bounds.

Maybe it feels a bit counter-intuitive, but follow the examples, and you'll see that it works:

```python
    # clip a value between lower bounds (0) and upper bounds (10)
    #
    oldValue = 3
    newvalue = max(0, oldValue)
    newvalue = min(10, newvalue)
    # result -> newvalue: 3
    #
    oldValue = -4
    newvalue = max(0, oldValue)
    newvalue = min(10, newvalue)
    # result -> newvalue: 0
    #
    oldValue = 35
    newvalue = max(0, oldValue)
    newvalue = min(10, newvalue)
    # result -> newvalue: 10
```

To put it more abstract:

```python
    # given:
    # value, a free ranging value
    # upperBounds, the upper bounds of the range
    # lowerBounds, the lower bounds of the range
    clippedValue = max(lowerBounds, value)
    clippedValue = min(upperBounds, clippedValue)
```

Or shorter on one line:

```python
clippedValue = max(lowerBounds, min(upperBounds, value))
```

Using the example above:

```python
newValue = max(0, min(10, oldValue))
```

## Wrap in range with modulo `%`

Sometimes you don't want to clip the value, because you might loose too much information outside the bounds. But you still need the value within a certain range. In some of these cases *wrapping* the value might be a good solution. Wrapping means that if the value tends to go outside the bounds, it will be wrapped inside again. (Starting at the beginning again, just like if you wrap a string around a sheet. If you wrap `12` to a value between `0` and `10` it will become `2`.)

Using value wrapping to keep a value inside a range, when the flow of the value is more important than the absolute order.

### `%` is the remainder of a division

To wrap a value, with start with the *modulo* function (`%`) which is the remainder of division.

If you divide `42` by `10` and you use only integers with the calculation, you get `4`.

> Side note: if you ask python to divide 42 by 10, like `42 / 10`, the output will be an integer (`4`), just like the components of the division. If you want the precision of a *float*, you should divide by a float, like `42 / 10.0` or `42 / float(10)`. This will result in `4.2000000`

The remainder of that division is `2`.

`42` minus the result of the division times the divider, or `42 - (4 * 10))` = `2`

Use the `%` symbol to quickly get that remainder, or modulo.

Some examples:

```python
42 % 10
> 2

43 % 10
> 3

10 % 3
> 1

99 % 20
> 19

100 % 25
> 0
```

[graph]

So if you want to wrap a value between `0` and a upper bounds, do the following:

`newValue = value % upperBounds`

#### Exercise

As an exercise, how would you wrap a value, if the lower bounds of the range to wrap to should not be `0`, but some other value? Write it as a formula. And give an example in code.

## Map from one range to another

What if you know the range of the input, and want to proportionally map a value from the input range to an output range?

In Processing and Arduino, there is the [*map*](https://www.arduino.cc/en/Reference/Map) function to do that. In python and plotdevice, there is none, so will write it ourselves. But in python there is already the build-in `map` function, which does something different. And on top of that in plotdevice, there is the [**translate**]("http://plotdevice.io/ref/Transform#translate()") function, which does only visual geometric translations.

So lets figure our a diffent name. Mabye `mapValue`?

[Stackoverflow](http://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another) helps with writing the function:

```python
def mapValue(value, fromMin, fromMax, toMin, toMax):
    # Figure out how 'wide' each range is
    fromSpan = fromMax - fromMin
    toSpan = toMax - toMin
    
    # Convert the from range into a 0-1 range (float)
    valueScaled = float(value - fromMin) / float(fromSpan)
    
    # Convert the 0-1 range into a value in the to range.
    return toMin + (valueScaled * toSpan)
```

