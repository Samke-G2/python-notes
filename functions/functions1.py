# Reusing Code with Functions              31/01/2025                  17:46

# Programs regularly need to perform the same task over and over.
# Instead of rewriting the same code, we can use FUNCTIONS to group related code and perform the task in one place

# To begin grouping related code, we start defining a function wiht the keyword 'def'
# Next, comes the function's name in snake case, followed by parentheses () .
# Like before, a colon : marks the beginning of the code block that belongs to the function.
# To group code into the function, we indent it by four spaces.
def greet_user():
    print("Good morning, Anna")
    print("Welcome back.")
    
# To run the code, we need to call the function. This is done by coding its naem followed by parentheses.
greet_user()


# Examples:

# 1
def weather_update():
    print("Weather update:")
    print("Sunny skies ahead")
    
weather_update()


# 2
def night_routine():
    print("Lights off")
    print("Alarm set")
    
night_routine()


# 3
def launch():
    print("3")
    print("2")
    print("1")
    print("Launch!")
    
launch()



# Creating Parameters               31/01/2025                  17:57

# Sometimes functions need specific information to help them perform their tasks.
# For a start, we can use variables inside functions
def greet_ron():
    name = "Ron"
    print(f"Hello, {name}")
    
greet_ron()


# How would we greet another person? We could create and call a new function greet_leslie() and similar code
def greet_leslie():
    name = "Leslie"
    print(f"Hello, {name}")
    
greet_leslie()


# Instead of writing two functions, we can pass specific information like "Leslie" to just one function, without repeating code.
def greet(name):
    print(f"Hello, {name}")
    
greet("April")
greet("Leo")


# To pass a value to a function, we first add a variable called a PARAMETER inside the parentheses of a function.
# The parameter acts like a variable that stores a value
# To pass a value to teh variable, we place it between the parentheses when we call the function
print("Example: using a parameter in a function - advanced, with input")

def greeting(name):
    print(f"Hello, {name}!")
    
user = input("Please enter your name: ")
greeting(user)


# Examples

# 1
def lamp_status():
    power = True
    print(f"Powered on: {power}")
lamp_status()

# 2
def display_half(num):
    half = num/2
    print(half)
display_half(10)

# 3
def double_number(num):
    result = num * 2
    print(result)

double_number(10)

# 4

    



