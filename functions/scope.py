# Functions and Variable Scope                  04/02/2025              17:15

# Variables created inside a function have a LOCAL SCOPE
print("Example 1: Local scope")

def add_bonus(salary):
    bonus = 100
    print(salary + bonus)
    
add_bonus(1900)

# With local scope, we can only access or update the variable within the function that created it
# If we try to access the variable outside of the function block, we'll get an error


# Variables created outside of a function block have a GLOBAL SCOPE
print("     ")
print("Example 2: Global scope")

shipping = 10

def calculate_total(cart):
    print(cart + shipping)
    
calculate_total(54)

# With a global scope, we can safely access the variable anywhere in the code, as we did with shipping
# All variables have a global scope, except for those created inside functions

# Even with global scope, it's important to note that we can only access variables after we've created them.
character ="Luigi"
print(f"Your character is: {character}.")

# Example
print("     ")
print("Global scope example")

price = 100
discount = 10

for i in range (2):
    price -= discount
    
print(f"Discount: R{discount}")
print(f"Price: R{price}")