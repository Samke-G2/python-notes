# Using Multiple Parameters                 02/02/2025                  22:07

# Functions need multiple parameters to perform tasks on more pieces of data, like a new player's first and last name
# We can already create functions with a single parameter
# To add more parameters to a function, we code a comma followed by the next parameter's name.
print("Example 1: Creating multiple parameters")

def display(first, last):
    print(first + " " + last)
    
display("Alex", "Morgan")
# To pass a second valjue to teh function, we code a comma followed by the value


# After adding the new parameter, and passing a matching value, we can use it in the function.
# We pass values to a function in the order of the parameters.
print("     ")
print("Example 2: Order of parameters")
def order(first, second):
    print(f"The first parameter is, {first}, and the second is, {second}.")
    
order("one", "two")


# We can add as many parameters as we'd like, as long as we seperate them with commas.
print("     ")
print("Example 3: Number of parameters")

def show_winners(gold, silver, bronze):
    print("First place: " + gold)
    print(f"Second place: {silver}")
    print(f"Third place: {bronze}")
    
show_winners("Kim", "Lee", "Ava")


# Examples
print("     ")
print("OVERARCHING EXAMPLES")

# 1
print("     ")
print("1")

def combine(one, two, three):
    return one + two + three

result = combine("big", "bad", "wolf")
print(result)


# 2
print("     ")
print("2")

def create_email(name, year):
    return name + year + "@hutmail.com"

output = create_email("jo", "1998")
print(output)


# 3
print("     ")
print("3")

def show_queue(current, next):
    print(f"now playing: {current}")
    print(f"up next: {next}")
    
show_queue("Stuck on you", "Jealous")

