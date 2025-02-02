# Returning Values                  02/02/2025              21:13

# A function can return a value to the code that called it.

# Functions are written to perform tasks and sometimes, we may need teh outcome of the tasks, this can be done via return.
# To return something from a function we add the 'return' keyword followed by the value to return
print("Example 1: Example of teh use of 'return' .")
def age_label(age):
    label = "User age: " + age
    return label

# A function can return ay type of values, like a string, integer, float, or boolean.
# We call teh returned value teh function's "output".
print("     ")
print("Example 2: The function's 'output' .")

def times_ten(num):
    result = num * 10
    return result


# We can use the return value of a function like any value by calling the function.
print("      ")
print("Example 3: Using the return value of a function.")

print(age_label("22"))


# We can also store the return value in avariable too.
result = age_label("29")
print(result)


# If we don't include a return statement, the function returns the value "none" instead.
def age_laebel2(age):
    label = "User age: " + age
    
result2 = age_laebel2("29")
print(result2)


# Examples

# 1
def give_me_ten():
    return 10

print(give_me_ten())

# 2
def add_greeting(user):
    greeting = "Greetings" + user
    return greeting

result = add_greeting("Sam")
print(result)

# 3
def half_twice(num):
    half = num/2
    half_again = half/2
    return half_again

# 4




