# Raising Exceptions (Part 1)                 19/02/2025                              16:46

# Sometimes we want to raise an exception when a condition we have defined is not met
print("       ")
print("Example 1.1: Raising an exception")

slices = 18
diners = 0
if diners < 1:
    raise Exception("There must be at least on diner")
else:
    slices_each = slices / diners
    

# The 'raise' keyword is used to raise an exception.
# We can define both the kind of error, and the error message, like here with ValueError
print("       ")
print("Example 1.2: Defining the type of error raised")

age = -3
if not age >= 0:
    raise ValueError("age cannot be negative")


# We can use exceptions to highlight when something cannot be working as it should be.
print("       ")
print("Example 1.3: Raising exceptions to highlight broken components")

predicted_sales = -5
if predicted_sales < 0:
    raise ValueError("predicted_sales cannot be negative")


# We can also use conditions to validate inputs, and raise an exception when the conditions are not met
print("       ")
print("Example 1.4: validating input and raising exceptions whe unexpected input is received")

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
except TypeError:
    raise TypeError("Input is not a number")
else: 
    if adult_years > 150:
        raise ValueError("Age is too large")
    
# 2
print("- - - - - - - - -")
print("2")

access = ["John", "Chloe", "Sandra"]
member = "Jennifer"

if member not in access:
    raise LookupError("Member not recognised")



# Raising Exceptions (Part 2)               20/02/2025                      18:41

# We often don't want a program to terminate when an exception is encountered. 
# A 'try and except' block can be used for EXCEPTION HANDLING
print("       ")
print("Example 2.1: Intro to 'try' and 'except' ")

def login(user):
    print(f"logged in, {user}")

try:
    login("user")
except LookupError:
    print("User not known, please try again")
    

# 'try and except' blocks tend to be used where we know there is a chance of the operation not being possible
print("       ")
print("Example 2.2: Using 'try' and 'except' ")

hours = []

try:
    average = sum(hours) / len(hours)
except ValueError:
    average = 0
    
print(average)


# 'try' and 'except' are followed by in indented block of code.
# We can use 'pass' if we want nothing to be executed after 'except'
user = "me"
try: 
    print("Hello, " + user)
except SyntaxError:
    pass


# The 'raise' keyword is used along with a valid type of error a nd an optional message
# It is usually used within an 'execpt' code block


# We can use an 'else' statement at the end if we weant to execute some code only when no error has been raised.
print("       ")
print("Example 2.3: Using the 'else' statement")

details = {
    "name": "Helena", 
    "occupation": "carpenter",
    "age": 35
}

try:
    age = details["age"]
except NameError: 
    raise NameError("No age value in record")
else:
    print(f"Maximum heart rate is {220 - age}")
    

# We can use a 'finally' statement at the end if we want to execute some related code regardless of whether an error was raised
print("       ")
print("Example 2.4: Using the 'finally' statement")

entry = 50

try:
    result = entry * 1.5
except ValueError:
    raise ValueError("result cannot be calculated")
else:
    print(result)
finally:
    print("Try another value?")


print("       ")
print("EXAMPLES")

# 1
print("- - - - - -")
print("1")
print("   ")

users = ["John", "Ellie", "Rachel", "Aubrey"]
user = "John"

try:
    users.index(user)
    print("Welcome back, " + user)
except LookupError:
    print("Do you want to become a member?")
finally:
    print("See our web site for offers for both members and non-members.")
    


