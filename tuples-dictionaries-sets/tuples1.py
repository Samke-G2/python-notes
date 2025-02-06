# Creating Tuples                       06/02/2025                          16:27

# Lists that contain pairs of data can be hard to read, and hard to discern which goes with which
movies = ["Vertigo", "Parasite", 1958, 2019]


# We can group related pieces of data with a tuple,
movies_tuple = [("Vertigo", 1958), ("Parasite", 2019)]


# TUPLES help us group different pieces of data that belong together
vertigo_data = ("Veritgo", 1958)

# Likewith list elements, we use commas , to seperate values in a tuple
# As a special case, tuples with only one value end in a comma anyway.
user_data = ("joe_17",)

print(user_data)

# Tuples can have as many values as we want
vertigo_data = ("Vertigo", 1958, "A. Hitchcock")

# We can save a tuple ina variable just like we do any other value
user_data = ("joe_17", "Joe Reed")

print(user_data)

# Parantheses surround the values of a tuple as square brackets surround the values of a list.
chai_blend = ("black tea", "cardamom", "ginger")



# Tuples and Lists (Part 1)                      06/02/2025                          17:20

# We can store tuples in a list just like any other values
print("     ")
print("Example 2.1: Storing tuples ina list")
scores = [("mia", 75), ("lee", 90)]

print(scores)


# We consider each tuple to be one value, so the length of teh 'scores' list is only 2
print("     ")
print("Example 2.2: using list methods on a tuple list")
print(len(scores))

# Just like with any other values, we use commas to seperate tuples in a list.
# We can access a specific tuple in alist by its index
print("     ")
print("Example 2.2: Accessing tuples in a list")
print(scores[0])


# Once we've accessed the tuple, we can save it in a variable
print("     ")
print("Example 2.3: Saving tuples ina variable")
mia_score = scores[0]
print(mia_score)


# We can use a 'for' loop or any other kind of loop to iterate over a list of tuples
print("     ")
print("Example 2.4: Looping through tuples ina list")

for user_score in scores:
    print(f"Result: {user_score}")
    
    
# Examples
print("   ")
print("EXAMPLES")

# 1
print("- - - - - -")
print("1")

cart = [("t-shirt", 40), ("jeans", 70), ("sweater", 90)]

print(cart)

# 2
print("- - - - - -")
print("2")

print(cart[1])

# 3
print("- - - - - -")
print("3")

item_3 = cart[2]
print(item_3)



# Tuples and Lists (part 2)                 06/05/2025                      17:36

# Let's look at similarities and differences between tuples and lists to know when to use one or the other.
event_tuple = ("Saturday", "21:00", "Anna's Bday")
days_list = ["Saturday", "Sunday"]


# Similarly to lists, we can access a tuple's values by their index
print("   ")
print("Example 3.1: Accessing a tuple element wiht an index")

print(event_tuple[1])

# The main difference is that unlike lists, we can't update, add, or delete values from tuples.
days_list[0] = "Friday"


# We say that tuples are IMMUTABLE, since trying to modify them results in an error
# Since tuples are immutable, we use them to store information that shouldn't be modified, like a person's name and birth date
personal_data = ("Anna", "21/05")

