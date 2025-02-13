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
print("EXAMPLES")

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



# Set Operations (PART 2)