# Deciding with functions               04/02/2025              17:35

# What if we wanted our functions to make a decision, like adding a shipping cost or not, based on whether the cart has a certain value or not?
print("Opening Example: A function that makes decisions")

def add_shipping(cart):
    if cart < 100:
        print(f"Total: {cart + 10}")
    else:
        print(f"Total: {cart}")
        
add_shipping(45)
add_shipping(200)

# When codinig a conditional inside the code block of a function, we say that we NEST it inside the function.
# To make a conditional work more flexibly, we can use the function's parameter as part of the condition.



#  Part 2                   04/02/2025                  17:52

# We can nest all kinds of conditionals inside functions
print("     ")
print("Example 2.1: Nesting other conditionals")

def calculate(operator, x, y):
    if operator == "+":
        print(x + y)
    else:
        print(f"unknown: {operator}")
        
calculate("-", 30, 10)
calculate("+", 30, 20)


# Even if the conditional is skipped, the remaining code in the function's code block runs
print("     ")
print("Example 2.2: The last line of a function")

def show_progress(points):
    if points > 1000:
        print("New highest score!")
    print("Ready for the next level?")
    
show_progress(900)



# Examples
print("     ")
print("EXAMPLES")

# 1
print("     ")
print("1")

def show_status(inbox):
    if inbox > 1000:
        print("Inbox full!")
    print("You have new messages!")
    
show_status(900)


# 2
print("     ")
print("2")

def show_notifications(score):
    if score < 30:
        print("Score too low")
    else:
        print("On to the next level!")
        
show_notifications(40)


# 3
print("     ")
print("3")

def show_score(score):
    if score < 30:
        print("Score too low")
    elif score == 100:
        print("Top score!")
    else:
        print("On to the next level!")
        
show_score(100)



