# Aliasing modules                          19/02/2025                      00:29
import statistics as stats
import math as math_constants
from time import sleep

# We can modify the name of the module we're importing
print("      ")
print("Example 1: Aliasing a module - changing its name when importing")

sales = [23, 43, 26, 26, 29, 18, 24]

median = stats.median(sales)
print(median)


# For that, we first code the 'import' keyword and module name as normal
# Then, we use the 'as' keyword to set the new name for the module

# Giving a new name to a module we're importing is known as aliasing
# It's often used to make longer module names shorter

# We also rename modules so that they don't interfere with variables in our code.
print("      ")
print("Example 2: Aliasing modules to avoid conflicts in variable names")

math = "Grade 12 constants"

print(math)

print("pi:")
print(math_constants.pi)

print("Euler's number:")
print(math_constants.e)


# To let our program wait, we need the 'sleep' module from the 'time' library
print("      ")
print("Example 3: Using sleep to delay code execution")

print("This message is shown immediately.")
sleep(1)
print("This message is shown after a 1-second delay.")

