# Code examples to Lesson 01: for loops

# Simplest form
for i in range(5):
    print i

# What is range
print range(10)
print range(5, 15)
print range(0, 10, 2)
print range(20, 0, -2)

# Loop through other lists
colors = ["white", "yellow", "orange", "red", "pink", "purple", "blue", "green", "brown", "black"]

for c in colors:
    print c
	
for c in colors:
    print c.upper()

# Nested for loops
# to filter a list

dont_likes = ["lettuce", "cabbage", "sesami", "sprouts"]
foods = ["tomatoes", "bananas", "cabbage", "lettuce", "spinach", "fries", "apples"]

# kids menu
for food in foods:
    include = True
    for bleh in dont_likes:
        if food == bleh:
            include = False
    if include:
        print food
