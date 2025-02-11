# Creating Dictionaries                       11/02/2025                             14:58   

# Dictionaries help create more nuance in related pieces of data.
# We use dictionaries to associate a meaning to each value in a collection of values
print("Opening Example: Example of a dictionary")

locations = {
    "headquarters": "New York",
    "flagship": "Paris"
}

print(locations)


# To create a dictionary, we start by coding a pair of curly braces {}
# Dictionaries are made up of of KEYS and VALUES, separayted by a colon   : 
# Inside the dictionary, we separate key-value pairs using commas  ,

# Keys are like labeled indeces. We use them because tehy help us retrieve values based on their meaning.
# Keys are unique within the dictionary, so we can only use a key once.
# Each key is associated with exactly one value 

# A dictionary's keys can be numbers, booleans, or tuples, but the most commonly used type is a string
print("     ")
print("Example 1: A dictionary with different data types")

car_data = {
    "brand": "Cadillac", 
    "year": 1960
}

print(car_data)


# The values can be of any type, including lists
print("     ")
print("Example 2: Lists in dictionaries")

car_data = {
    "brand": "Cadillac", 
    "year": 1960,
    "restoration": ["1990", "2018"], 
    "rented": False
}

print(car_data)

# We can store as many key-value pairs as we want inside a dictionary.



print("     ")
print("EXAMPLES")

# 1
print("- - - - - - -")
print("1")
user = {
    "name": "Gilles",
    "surname": "Rosby"
}

# 2
print("- - -- - - - - ")
print("2")
contents = {
    "ch. 1": "A long-expected party",
    "ch. 2": "The shadow of the past",
    "ch. 3": "Three is company"
}

print(contents)

# 3
print("- - - - - - ")
print("3")
participants = {
    "Meg": True,
    "Kim": False, 
    "Luis": True,
    "Luis M.": False
}

print(participants)

# 4
print("- - - - - - - -")
print("4")
members_count = {
    ("Sai", "Chloe", "Yumi"): 3
}

print(members_count)

# 5
print("- - - -  - - - -")
print("5")

winner_score = {
    "first": ("Ted", 50), 
    "second": ("Jess", 47)
}

print(winner_score)

# 6
print("- - - - - - - - ")
print("6")

air_composition = {
    "nitrogen": "78%", 
    "oxygen": "21%", 
    "argon": "0.93%", 
    "carbon dioxide": "0.04%", 
    "other": "0.03%"
}


