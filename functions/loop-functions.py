# Functions with Loops (Part 1)                 05/02/2025                  17:11

# Functions help us reuse loops by allowing us to change the number of repititions or the list we're iterating through
print("Example 1.1: Using a while loop in a function")

def onboard_passengers(bookings):
    counter = 1
    while counter <= bookings:
        print(f"Passenger {counter} on board")
        counter += 1
        
onboard_passengers(4)


# We can use both 'while' and 'for' loops inside functions
print("        ")
print("Example 1.2: Using a 'for' loop in a function")

def display_progress(total_files):
    for i in range(total_files + 1):
        print(f"Downloading file {i} out of {total_files}")
        
display_progress(3)



# EXAMPLES
print("    ")
print("EXAMPLES")

# 1
print("- - - - - - - -")
print("1")
print("  ")

def do_countdown(counter):
    while counter > 0:
        print(counter)
        counter -= 1
    print("Go!")
    
do_countdown(3)

# 2



# Functions with Loops (Part 2)                 05/02/2025                  17:41

# Ranges like range(3) tell us how many times the 'for' loop runs
print("       ")
print("       ")
print("Example 2.1: Using a range in a function")
def display_progress():
    for i in range(4):
        print(f"Downloading file {i} out of 3")
        
display_progress()


# To reuse a 'for' loop with any range, we pass a parameter between the parantheses of range()
print("       ")
print("Example 2.2: Reusing a 'for' loop")

def display_progress(total_files):
    for i in range(total_files + 1):
        print(f"Downloading file {i} out of {total_files}")
        
display_progress(5)

# The value we pass when calling the function is stored in the parameter and then used as a range



# Functions with Loops (Part 3)                05/02/2025                   17:53

# To reuse a loop that iterates through a list, we can nest it in a function
print("      ")
print("      ")
print("Example 3.1")
def halve_prices(cart):
    for price in cart:
        print(f"New price: {price/2}")
        
cart_list = [5, 28, 8]
halve_prices(cart_list)

# To loop through any kind of list, we use the function's parameter instead of a fixed list
# By looping through the list in the parameter, we can call the function with any list


# EXAMPLES
print("      ")
print("PART 3 EXAMPLES")

# 1
print("--------")
print("1 ")

def display_players(team):
    number = 1
    for name in team:
        print(f"Player {number}: {name}")
        number += 1
        
team_1 = ["Kim", "Lee"]
team_2 = ["Meg", "Jo"]

print("team 1:")
display_players(team_1)

print("team 2:")
display_players(team_2)

