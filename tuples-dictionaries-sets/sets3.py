# Sets and Lists                        14/02/2025                          00:38

# Unlike sets, lists allow duplicates
# To eliminate duplicates from a list, we can transform it into a set with set() by putting the list name in the parentheses
print("     ")
print("Example 1: Transforming a list into a set")

grocery_list = ["broccoli", "cereal", "milk", "broccoli"]

print(set(grocery_list))


# Used on a list, set() gives a set of the unique list values which we can then store in a variable
grocery_set = set(grocery_list)


print("- - - - - - - ")
print("EXAMPLES")

# 1
print("- - - - - - - ")
print("1")

drinks_list = ["matcha", "chai", "chai", "espresso", "americano", "chai", "matcha"]

drinks_set = set(drinks_list)
print(drinks_set)


