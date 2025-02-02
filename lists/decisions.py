# Deciding with Lists               30/01/2025              16:23

# Let's find out how we can count the elememts in lists and use them with 'if' statements

# We use the len() instruction with the list name in parentheses to get the number of elements in a list.
users = ["Sarah", "Mike", "Ella"]

print(len(users))

# We can store the length of a list ina variable
users = ["Sarah", "Mike", "Ella"]

number_of_users = len(users)

print(number_of_users)

# If we use len() on an empty list it'll return 0. 

# We can use list length to create conditional statements based on the number of elements
tasks = ["dishes", "windows", "vacuum"]

if len(tasks) > 0:
    print("Ugh, more work!")
    
