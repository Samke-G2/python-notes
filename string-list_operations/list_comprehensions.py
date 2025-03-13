# Using List Comprehensions                     26/02/2025                      14:10

# To create a list based on another, we need to first create an empty list, then fill it inside a loop
print("     ")
print("Example 1: Filling a list with a loop ")

prices = [10, 38, 40, 58, 62]
halved = []

for price in prices:
    half_price = price/2
    halved.append(half_price)

print(halved)


# We can build the same halved list as before, but in one line, using list comprehensions.
print("     ")
print("Example 2: Using a list comprehension ")

halved2 = [price/2 for price in prices]

print(halved2)

# The list comprehension is an equivalent, but more compact version of the code with the loop
#A list comprehension is a way to create a new list by applying an expressiion on each element of an existing list.

# Since a list comprehension returns a new list, we start with square brackets []
# List comperhensions use a 'for' loop to iterate through each element of the original list
# Like any 'for' loop, there is an variable that holds the list elements one by one and a list we're looping over.
# At the beginning of the list comprehension, we write an expression to apply on each element of the list
# By assiging a list comprehension to a variable, we're actually saving the resulting list into the variable


print("     ")
print("EXAMPLES")


# 1
print("- - - - - -")
print("1 ")

flights = ["1122", "5788", "0044"]
print(f"Original flights list: {flights}")

print("New list produced by list comprehension: ")
codes_lc = ["BA" + flight for flight in flights]
print(codes_lc)

print("list produced by 'for' loop: ")
codes_loop = []
for flight in flights:
    code = "BA" + flight
    codes_loop.append(code)
print(codes_loop)

print(f"Are they the same? : {codes_lc == codes_loop}")


# 2
print("- - - - - -")
print("2 ")

meters = [100, 3800, 4000]

kilometers = [m/1000 for m in meters]

print(kilometers)


# 3
print("- - - - - -")
print("3 ")

miles = [100, 57, 40, 20]

km = [value * 1.609 for value in miles]

print(km)


# 4
print("- - - - - -")
print("4 ")

answers = [True, False, False]

opposite = [not answer for answer in answers]

print(opposite)


# 5
print("- - - - - -")
print("5 ")

expiry_years = [2018, 2020, 2019]

renewed = [year + 4 for year in expiry_years]

print(renewed)

# 6
print("- - - - - -")
print("6 ")

ages = [15, 20, 19]

can_drive = [age >= 18 for age in ages]

print(can_drive)
