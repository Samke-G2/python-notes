# Functions as Expressions                  13/03/2025                      19:51

# We can use a list comprehension to create a new list by applying a function to each element of an existing list.
# We start by iterating through each element in a list with a for loop
# We can pick the operations we want to apply to each value in a function and use that as an expression in a list comprehension
print(" ")
print("Example 1: Using a function in a list comprehension")

prices = [10, 22, 30, 40, 58, 62]

def halve(num):
    return num/2

halved = [halve(price) for price in prices]

print(halved)


# Functions are useful when we want to apply more expressions, like removing tax then halving price
print(" ")
print("Example 2: applying mor operations with a function")

def halve2(num):
    no_tax = 0.85 * num
    return no_tax/2

halved = [halve2(price) for price in prices]

print(halved)


# We can only use function that have return statements since we're actually appending the returned value to the new list 
print(" ")
print("Example 2")

authors = ["Virginia Woolf", "John Steinbeck", "Chinua Achebe", "Chimamanda Adichie"]

def add_comma(name):
    parts = name.split()
    return parts[1] + ", " + parts[0]

authors_update = [add_comma(name) for name in authors]

print(authors_update)


