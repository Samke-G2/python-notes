# Set Operations (PART 1)                    14/02/2025                          00:51

# Just like with lists, we can get the size of a set with the len() instruction
print("     ")
print("     ")
print("Example 1.1: Finding the length of a set")

friends = {"Emma", "Jen", "Rob", "Ed"}
print(len(friends))


# When all elements of a set are present in another set, we say that it is a SUBSET of that set
print("     ")
print("Example 1.2: Subsets")

chat = {"Jen", "Ed"}        # 'chat' is a subset of 'friends'

# To check whether a set is a subset of another, we code the name of the set, then .issubset() with the name of the other set between parentheses
print("     ")
print("Example 1.3: Checking if a set is a subset of another")

print(chat.issubset(friends))
# issubset returns True if the left set is a subset of teh right, otherwise it returns False
study_group = {"Emma", "Lisa"}

print(study_group.issubset(friends))

# We can save the boolean given by issubset() in a variable
are_friends = study_group.issubset(friends)
print(are_friends)


print("     ")
print("EXAMPLES (PART 1)")

#1
print("- - - - - - ")
print("1")

invitations = {"Meg", "Alex", "Lee"}

print(f"{len(invitations)} invitations sent")


# 2
print("- - - - - - - ")
print("2")

animals = {"whale", "dog", "cat", "giraffe"}
pets = {"dog", "cat"}

print(pets.issubset(animals))



# Set Operations (PART 2)                       18/02/2025                          16:37

# We can join two sets using 'union()'.
print("      ")
print("Example 2.1: Using union() ")

classmates = {"Sue", "Paul"}
friends = {"Don", "Sue"}

print(classmates.union(friends))
# Union() gives us a new set without duplicates, even if some  elements are present in both original sets.


# Similarly, we can use 'intersection()' to create a set of elements that are present in both sets
print("      ")
print("Example 2.2: Using 'intersection()' ")

classmates = {"Sue", "Luke", "Paul"}
friends = {"Don", "Sue", "Luke"}

print(classmates.intersection(friends))


# While union() gives us all elements of the two sets, 
# intersection() gives us only the common ones
print("      ")
print("Example 2.3: The difference between intersection and union")

print("Union: ")
print(classmates.union(friends))

print("Intersection: ")
print(classmates.intersection(friends))


# We can save the sets given by union() and intersection() in variables 
print("      ")
print("Example 2.4: Saving the result sets in variables")

everybody = classmates.union(friends)

common = classmates.intersection(friends)


print("      ")
print("EXAMPLES (PART 2)")

# 1
print("- - -  - - -")
print("1")

arrivals = {"JL5273", "NH5753"}
departures = {"AA5827", "BA4616"}

all_flights = arrivals.union(departures)
print(all_flights)


# 2
print("- - - - - - -")
print("2")

visited = {"Paris", "New York", "Tokyo"}
holiday_plans = {"Rome", "Paris"}

destinations = visited.intersection(holiday_plans)
print(destinations)



# Set Operations (PART 3)                       18/02/2025                          17:29

# To get a set of elements that are pressent in one set, but not another, we use the 'difference()' instruction
print("      ")
print("Example 3.1: using 'difference()' ")

print(classmates.difference(friends))


# Using difference() gives us the elements that the left set has, but the right set doesn't.
print("      ")
print("Example 3.2: how the 'difference()' instruction works")

team_1 = {"Alpha", "Beta", "Theta"}
team_2 = {"Alpha", "Beta", "Charlie", "Delta"}

print(team_1.difference(team_2))

# Changing the order of the sets inputed changes the results of using 'difference()'
print("      ")
print("Example 3.3: changing the order of inputs in 'difference()' ")

print(team_2.difference(team_1))


# We can save the set obtained in a variable 
print("      ")
print("Example 3.4: Saving the set obtained in a variable")

friends_not_classmates = friends.difference(classmates)
print(friends_not_classmates)



print("      ")
print("EXAMPLES (PART 3)") 

# 1
print("- - - - - - - ")
print("1")

animals = {"whale", "dog", "cat", "giraffe"}
pets = {"dog", "cat"}

not_pets = animals.difference(pets)

# 2
wishlist = {"earpods", "notebook", "handgloves"}
cart = {"cat food", "book", "earpods"}

print(wishlist.difference(cart))
print(cart.difference(wishlist))


