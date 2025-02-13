# Using Variables (PART 1)                      13/02/2025                      23:46

# To add a new value to a set, code 'add()' with the new value between teh parentheses.
# Note that elements in sets are unordered, hence we can't be sure in which order the items will appear when printed.
print("     ")
print("Example 1.1: Adding a new value into a set")

answers = {"yes", "no"}
answers.add("maybe")

print(answers)


# Since sets exclude duplicates, nothing happens when we use add() with an already existing value


print("     ")
print("EXAMPLES - 1")

# 1
print("- - - - - - - -")
print("1")

subscribers = {"jess@mail.com", "meg@mail.com"}
subscribers.add("luke@mail.com")

print(subscribers)

# 2
print("- - - - - - - ")
print("2")

wishlist = {"earpods", "notebook", "handgloves"}
wishlist.add("notebook")

print(wishlist)



# Using Sets (PART 2)                           13/02/2025                      23:57

# We can update elements in lists by their index.
# Unlike lists, sets are unordered, meaning that set elements don't have indices.

# Since sets don't have indices, we can only check if a set contains an element with the 'in' keyword
print("     ")
print("Example 2.1: Using the 'in' keywords to check the contents of a set")

answer_options = {"yes", "no"}

print("no" in answer_options)


# We can also use a 'for' loop to iterate through set elements and access them one-by-one
print("     ")
print("Example 2.2: using a for loop to access set elements")

for answer in answer_options:
    print(f"Option: {answer}")
    

print("     ")
print("EXAMPLES")

# 1
print("- - - - - - -")
print("1")

networks = {"May's", "PizzaParty5", "Wi-Free"}

for network in networks:
    print(f"Connect to {network}")
    


# Using Sets (PART 3)                      14/02/2025                           00:29

# To remove a set element like "Music", we code the set name followed by .remove() with the element between parentheses
print("- - - - - - -")
print("Example 3.1: Removing a set element")

classes = {"Geometry", "Music", "French"}
classes.remove("Music")

print(classes)


# To avoid getting an error, first check if an element is in a set before removing it 
if "History" in classes:
    classes.remove("History")
    
print(classes)


