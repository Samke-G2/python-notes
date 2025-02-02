# Self-assigning and Operators                  25/01/2025                  21:00


# This is a powerful concept which explains how variables keep track of things like adding or removing dollars from a wallet
# When we create a variable, we assign it a value
wallet = 3

# self-assigning is when we set a variable to its own value.
wallet = wallet

# Because we can self-assign variables, we can increase or decrease variables set to numbers.
wallet = wallet + 1
print(wallet)

# self-assigning variables let us track data that changes over time.
wallet = wallet + 2
wallet = wallet - 1

print(wallet)

# Variables set to strings work the same way.
name = "Account name: "
name = name + "Elton"
name = name + " John"

print(name)



# Part 2                        25/01/2025                      21:10


# Since self-assigning is a powerful tool for building programs, lets learn a few operators that help us write code faster.
# We know that we can add to a variable by writing out the variable name.

# Rather than rewriting the variable's name, we can use the += operator to add to a variable.
sales = 5
sales += 1

print(sales)


# To subtract from a variable's value, we use the -= operator
sales = 5
sales -= 3

print(sales)

