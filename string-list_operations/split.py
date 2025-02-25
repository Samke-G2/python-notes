# Splitting a strings                   25/02/2025                          17:25

# When working with different kinds of data,
# We can receive it in a format that makes it hard to work with.
# Like trying to work with inndividual words in a sentence-like string value.

# We're able to split up strings and store the individual values in a list by codint ' .split() '
print("     ")
print("Example 1: Splitting string with the '.split()' method")

new_users = "Rob Jon Sansa Arya Bran Rickon"

users_list = new_users.split()


# We can store the individual elements of a split string into a list.
# and print them by printing the list
print(users_list)

# Strings are separated on whitespace by default.


# We can specify exactly how we want to split a string by placing a separator inside the parentheses
print("     ")
print("Example 2: Splitting a string at a separator")

user = "Lauren,25,F,Architect"
user_1 = user.split(",")

print(user_1)



print("     ")
print("EXAMPLES")

# 1
print("- - - - - ")
print("1 ")

area_codes = "1150 1190 1100 1700"
code_list = area_codes.split()

print(code_list)

# 2
print("- - - - -")
print("2 ")

sales = "24k 29k 7k"
sales_list = sales.split()

print(sales_list)

# 3
print("- - - - - ")
print("3")

temps = "34 23 44"
temps_list = temps.split()

print(temps_list)

# 4
print("- - - - -")
print("4 ")

pollution = "55ppm 44ppm 22ppm 66ppm"
pollution_list = pollution.split()

print(pollution_list)

# 5
print("- - - - - ")
print("5")

path = "mimo.org/courses/python"
path_list = path.split("/")

print(path_list)
