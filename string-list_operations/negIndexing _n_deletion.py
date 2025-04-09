# Negative Indexing and Deletion                        09/04/2025                      17:21

# Python allows us to use negative indexing to retrieve values from the end of an indexable object, such as a list.
print("    ")
print("Example 1 : negative indexing at work")

scores = [4.5, 5, 3, 4, 3.5, 4]

latest = scores[-1]
print(latest)

# Negative indexing means that we retrieve an element from the rightmost side of a list.
# We use the -  symbol to indicate a negative index
print(" -- ")

users = ["Tony", "Tina", "Tom"]

last = users[-1]
print(last)


# We can use any value up to and including the length of the list, which would retrieve the first value
print("    ")
print("Example 2: Using negative indexing ")

ratings = [4, 5, 3, 1, 2, 3]

print(ratings[-6])


# We can also modify list items in the given position
print("    ")
print("Example 3: Modifying using negative indexing")

white_users = ["Jack", "Achmed", "Elaine"]

users[-2] = "Jill"
print(white_users)

# Tuples are also ordered data structures and values can be retreived, but they are immutable and so cannot be modified
print("    ")
print("Example 4: Negative indexing a tuple")

info = ("Graz", "Autria", "Europe", "World")
print(info[-4])


# We will encounter an error if we attempt to retrieve a value in a position outside the object's range


# The "del" keyword allows us to delete objects, or items within a data structure
print("    ")
print("Example 5: Deletion at work ")

winners = ["John", "Helen", "Sigmund", "Olaf"]
print(winners)

del winners [-1]
print(winners)


# "del" can be used to delete any object, including data structures such as dictionaries, lists, and sets
letters = {"a", "b", "c"}

del letters
# print(letters)                - Trying to print the "letters" dictionary will result in an error since we deleted it

 
