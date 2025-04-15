# Slice Notation                        15/04/2025                      15:49

# Sometimes we want to retrieve multiple values from a list.
# We can do this using slicing.
print(" ")
print("Example 1: using the [start:stop] slicing notation")

ingredients = ["eggs", "flour", "sugar", "salt"]
print(ingredients[0:2])


# The value to the left of the colon :  is the start position for the slice.
# As we've covered previously, Python indexing statrts at zero
print(" ")
print("Example 2: The start position")

letters = ["A", "B", "C", "D", "E"]
print(letters[4:])
print(letters[1:])
# By coding just the start position, we've retrieved all values beginning at that list position to the end of the list.


# The start value can be positive, negative, or omitted completely.
# Negative values mean "start this many elements back from the end".
print(" ")
print("Example 3: Using different types of indexing in slice notation")

users = ["Alan", "Beth", "Carla", "Dennis"]

print(f" posistive(0) = {users[0:]} ")
print(f" omitted = {users[:]} ")
print(f" negative = {users[-2:]} ")


# Specifying a range outside the length of the list as a starting index will return an empty list, rathe rthan resulting in an error.
print(" ")
print("Example 4: start index outside of the list length")

print(letters[6:])


# The value after the colon : represents where the slice should STOP.
# Note that the element in hte stop position is NOT included.
print(" ")
print("Example 5: Using a stop value")

scores = [50, 40, 30, 20, 10]

print(scores[:2])
print(scores[2:4])


# If we use a start value of 0(or do not include one), a positive stop value will be equal to the number of elemetns returned.
print(" ")
print("Example 6: Returning a certain number of elements")

print(letters[:3])


# A start index that is greater than the stop index in the [start:stop] format won't result in an error, but will return an empty list.
animals = ["antelope", "bear", "cat", "dog"]

print(animals[3:0])


# We can also use a format with two colons, [start : stop : step]
# where "step" determines how Python steps between start and end.
print(" ")
print("Example 7: Using 'step' ")

alphabet = ["A", "B", "C", "D", "E", "F"]

print(alphabet[1:6:2])
# A step of :2 means that instead of returning every value in hte slice, we return every second value.
# A step of :3 would mean every third value
print(" ")
print("example 7 continued... 3 step")

print(alphabet[1:6:3])


# We can use the step value with no start or end values.
# By default this will work from the start to the end of the full original list.
print(" ")
print("Example 8: using rhe step value on it's own")

friends = ["Anna", "Bella", "Carrie", "Diana", "Eleanor"]

print(friends[::2])


# Each value can be positive, negative, or omitted completely.
# To use the step value, we must always have two preceeding colons
print(" ")
print("Example 9: Using different types of indeces with the step")

flowers = ["azalea", "buttercup", "carnation", "daffodil"]

print(flowers[2::-1])
print(flowers[:3:2])


# Step can be negative, which allows us to use a start value larger than the end value.
# The order of the elements is reversed
print(" ")
print("Example 10: Larger start than end, with negative step")

print(friends[3:0:-1])


# If no start or end value are given, Python will automatically work from the end of a list if a negative step value is provided.
print(" ")
print("Example 11: negative step with no start or end")

countries = ["Andorra", "Brazil", "China", "Denmark", "Egypt"]

print(countries[::-3])


# 


