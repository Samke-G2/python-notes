# Using Dictionaries (PART 1)                  11/02/2025                  17:19

# We access dictionary values by their key
# To access a value, we code the dictionary's name and then the key between square brackets
print("     ")
print("Example 1.1: Accessig values by their key")

actor_bio = {
    "name": "Bill Murray",
    "known for": ["Lost in translation", "Rushmore"]
}

print(actor_bio["known for"])

# After accessing a avalue, we can store it in a variable
actor_name = actor_bio["name"]
print(actor_name)


# We can loop throughthe dictionary keys with a 'for' loop.
print("     ")
print("Example 1.2: Looping through a dictionary's keys")

player_scores = {
    "ann": 13,
    "michael": 20,
    "ava":34
}

for player in player_scores:
    print(f"{player}'s score is {player_scores[player]}")
    
    
# To update the value associated with a key, we start by accessing it.
# Then we update it like we would any variable, by coding  =   then the new value
print("     ")
print("Example 1.3: Updating a value in a dictionary")

ticket = {
    "seat no.": 25,
    "first class": False
}

ticket["first class"] = True
print(ticket)




# Using Dictionaries (PART 2)                11/02/2025                         17:37

# To add a key, we code the dictionary's name and then the neykey's name between square brackets
# To associate the new key with a value, we code an equal = followed by the value.
print("     ")
print("Example 2.1: Adding a new key-value pair to a dictionary")

tickets = {
    "seat no.": 25
}

tickets["window"] = True
print(tickets)
# Adding a new key-value pair resembles updating, with the difference being that the key is not yet in the dictionary



# Using Dictionaries (PART 3)               13/02/2025                       17:32

# To check if a dictionary contains a certain key, we use the 'in' keyword
print("     ")
print("Example 3.1: Using the 'in' keyword")

personal_data = {
    "name": "Mac Miller",
    "telephone": "0047865791"
}

print("name" in personal_data)
# As with lists, the keyword gives True when the key is present, and False otherwise


# We can store the information of whether a key is present in the dictionary in a variable
print("     ")
print("Example 3.2: Storing the result of the 'in' keyword in a variable")

has_address = "address" in personal_data
print(has_address)



# Using Dictionaries (PART 4)               13/02/2025                        17:06

# We remove a key-value pair similarly to removing an element from a list, by coding the dictionary name and then teh '.pop()' instruction
print("     ")
print("Example 4.1: Removing a key-value pair from a dictionary")

stock = {
    "dresses": 25,
    "t-shirts": 50,
    "jeans": 1
}

# stock.pop()
# print(stock)


# When using '.pop()' with dictionaries, we need to specify which key we want to remove
print("     ")
print("Example 4.2: Specifying a key to remove")

stock.pop("jeans")
print(stock)


# We can store the value of the removed key in a variable
print("     ")
print("Example 4.3: Storing the value of the removed key in a variable")

jeans_stock = stock.pop("jeans")
print(jeans_stock)


# Attempting to remove a key that doesn't exist gives us an error
print("     ")
print("Example 4.4: Attempting to remove a key that doesn't exist")

# stock.pop("caps")


# To avoid getting an error when removing a key, it's good practice to first use the 'in' keyword to check if the key exists
print("     ")
print("Example 4.5: Using the 'in' keyword to check if a key exists in a dictionary")

if "dresses" in stock:
    stock.pop("dresses")
    
print(stock)





