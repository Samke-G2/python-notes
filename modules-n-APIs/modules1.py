# Modules (Part 1)                      18/02/2025                  23:29
import math
import statistics

# Classes are a way to organize data and functionality together
print("      ")
print("Example 1.1: Example of a class")

class Car:
    wheels = 4
    doors = 4
    
    def start_engine(self):
        print("Vroom!")
        
my_car = Car()
print(my_car.wheels)
my_car.start_engine()


# We can add more organisation to our code with something called MODULES
print("      ")
print("Example 1.2: Intro to modules - math.pi")

print("The value of pi is")
print(math.pi)


# Modules group related classes and data and make them accessible from one place
print("      ")
print("Example 1.3: Using modules - math.sprt")

print("The square root of 16 is")
print(math.sqrt(16))


# Python has a lot of built-in modules.
# The math module provides data, like the value of pi,
# and methods for different math operations.


# To use a module, we import it with the keyword 'import' followed by the module's name

# To use the module, we add its name followed by the method or data we want



print("      ")
print("EXAMPLES (PART 1)")

# 1
print("- - - - - - - ")
print("1")

print("Rounded up to the nearest number")
rounded = math.ceil(22.7324)

print(rounded)



# Modules (Part 2)                      19/02/2025                        00:07

# Statistics is another built-in module
# It helps out with statistic functions like the mean of a list
print("      ")
print("Example 2.1: Using the statistics module - mean")

scores = [4, 4, 3, 6, 1, 2, 8, 4]
mean = statistics.mean(scores)

print(f"Mean score is {mean}")


# We are able to use different modules in the same file by adding a comma between the modules we're importing
print("      ")
print("Example 2.2: importing multiple modules ina  single file")

diameters = [9, 7, 4, 6]
result = statistics.mean(diameters)
print(f"Mean diameter is {result}")

print("Value of pi is:")
print(math.pi)


# Sometimes we want to use just parts of a module, and not the whole functionality.
# In that case, we can use the keyword 'from' to extract only the functionality we care about

# from math import pi

# When we use 'from' , we don't need to add the name of the module anymore
# like using mean instead of statistics.mean

# result = mean(test_scores)




