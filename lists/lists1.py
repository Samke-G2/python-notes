# Grouping data in lists                29/01/2025                  17:46

# Being able to organize lots of related data is an essential part of data science.
# If we had to create a variable for every piece of new data, our code would get very long and complicated.

todo_1 = "Read"
todo_2 = "Workout"
todo_3 = "Code"
todo_4 = "Meditate"

# Rather than creating a variable for each new piece of data, we can collect related data inside a list using [ and ].
print("Example 1: Creating a list")

todo = ["Read", "Workout", "Code"]
print(todo)

# The values inside a list are called ELEMENTS of the list.
# We can also create empty lists by coding just the [ and ]
# We use commas to seperate two or more values in a list.
# We can store as many values as we want in a list.


# Examples

# 1
active_users = ["Jake", "Finn", "Simon"]
print("Active: ")
print(active_users)



# Changing Data in Lists                29/01/2025                  17:58

# Let's dig deeper into managing lists and how to update the data inside them, like how temperature data might change throughout the day.
temperatures = [17, 20, 26, 24]

# Lists can store any piece of data, be it string, boolean, float, or integer

# Every element in a list has a numbered position called an index
index = [0, 1, 2, 3, 4, 5]

# Indices start at zero and increase with each further value. That means that the second element in temperature is at index [1]
print(temperatures[1])

# To change an element value in the list we access it using the index, then use the = to assign it a new value
temperatures[2] = 25
print(temperatures)



# Updating Lists                        29/01/2025                  18:10

# Let's learn how to add and remove values in a list


# To add a new value to a list, we code the list name followed by a full stop . , then the instruction append() with the value in the parentheses.
print("Example 1: append()")

scores = [24, 23]
scores.append(25)
print(scores)

# Adding a value with .append() places it at the end of the list. 
users = ["john", "hannah", "marco"]
users.append("julian")
print("users")

#We add a value to a specific index with .insert(), by coding the index first then the value after a comma inside the brackets
print("Example 2: insert()")

shopping = ["kiwis", "peas"]
shopping.insert(0, "lemon")
print(shopping)

# The insert() function has two parameters
# first the index where we want to insert the value, followed by the value.
print("--")

shopping.insert(1, "chocolate")
print(shopping)

# For both .append() and .insert(), we can only add one element at a time.


# To remove the last element of a list, we code the list name, a full stop, and the instruction pop()
print("Example 3: pop()")

todo = ["call mom", "dishes"]
todo.pop()

print(todo)

print("-----")

# To remove a value at a specific index, we add the index we want to remove in parentheses
todo = ["call mom", "dishes", "painting"]

todo.pop(1)
print(todo)

# The removed value can be stored inside a variable too.
todo = ["call mom", "dishes", "painting"]

removed = todo.pop(0)
print(removed)

