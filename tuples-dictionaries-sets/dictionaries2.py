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

ticket["window"] = True
print(ticket)
# Adding a new key-value pair resembles updating, with the difference being that the key is not yet in the dictionary



# Using Dictionaries (PART 3)               11/02/2025



