# Raising Errors                            19/02/2025                              16:46

# Sometimes we want to raise an exception when a condition we have defined is not met
print("       ")
print("Example 1: Raising an exception")

slices = 18
diners = 0
if diners < 1:
    raise Exception("There must be at least on diner")
else:
    slices_each = slices / diners
    

# The 'raise' keyword is used to raise an exception.
# We can define both the kind of error, and the error message, like here with ValueError
print("       ")
print("Example 2: Defining the type of error raised")

age = -3
if not age >= 0:
    raise ValueError("age cannot be negative")


# We can use exceptions to highlight when something cannot be working as it should be.
print("       ")
print("Example 3: Raising exceptions to highlight broken components")

predicted_sales = -5
if predicted_sales < 0:
    raise ValueError("predicted_sales cannot be negative")


# We can also use conditions to validate inputs, and raise an exception when the conditions are not met
print("       ")
print("Example 4: validating input and raising exceptions whe unexpected input is received")

scores = [125, 60, 189, 88, 16]

if min(scores) < 0 or max(scores) > 180:
    raise ValueError("Error in scores")



print("       ")
print("EXAMPLES")

# 1
print("- - - - - - - - -")
print("1")

age = 1000
try:
    adult_years = age - 18
except:
    raise TypeError("Input is not a number")
else: 
    if adult_years > 150:
        