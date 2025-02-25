# Updating Strings                      25/02/2025                          18:01

# Sometimes we'll need to update data inside a string without creating a whole new string
# We can replace a part of a string stored inside a variable by using the '.replace()' method
# Inside the parentheses, we add teh part we want to replace, a comma, and then the new value
print("     ")
print("Example 1: Using the .replace() method")

special = "Today's special is pasta"

new_special = special.replace("pasta", "pizza")

print(special)
print(new_special)

# Instead of creating a new variable, we can reassign the original variable to the updated string
special = special.replace("pasta", "pizza")
print(special)


# When we use replace() like this, we'll replace all occurences of the value inside the string.
print("     ")
print("Example 2: Replacing all occurences of the value inside a string")

june = "June sales target updated. Let's rock June!"
july = june.replace("June", "July")

print(july)


print("     ")
print("EXAMPLES")

# 1
print("- - - - - ")
print("1")

age_group = "twenty-five to thirty"

updated = age_group.replace("thirty", "thirty-five")

print(updated)
