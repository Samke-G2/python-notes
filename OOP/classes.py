# Using Classes                     24/04/2025                      16:40

# As we build programs, we'll often need to create many similar but distinct objects.
# Like various different configurations of a computer.
print(" ")
print("Example 1: Why we need classes")

computer1_size = "15"
computer1_storage = "1TB"

computer2_size = "13"
computer2_storage = "256GB"

print("computer1 display size: " + computer1_size)
print("computer1 storage space: " + computer1_storage)

print("computer2 display size: " + computer2_size)
print("computer2 storage space: " + computer2_storage)

# creating new variables for each of the different configurations of a computer would take a lot of time and could lead to mistakes.


# To help us group data and functionality, we create a class.
# A class is a template that we use to create many similar, but distinct things.
print(" ")
print("Example 2: Creating a class")

class Computer:
    def __init__(self, size, storage):
        self.size = size
        self.storage = storage
        
    def print_specs(self):
        print("Display size: " + self.size)
        print("Storage size: " + self.storage)
        
low_spec = Computer("13", "256GB")
high_spec= Computer("27", "1TB")

print("Low Spec Computer: ")
low_spec.print_specs()

print("High Spec Computer: ")
high_spec.print_specs()

# By using a template, we can create different configurations without having to create individual variables each time.


# To start creating the template we add the keyword 'class' followed by a name and a colon.
# To add code to the class, we indent from the keyword 'class'.
# Creating a variable inside a class works just like creating normal variables. 
    #It just needs to be properly indeneted and assigned a value.
# We can add as many variables as we'd like inside a class.
print(" ")
print("Example 3: step-by-step of creating a class ")

class Person:
    nationality = "South African"
    hobby = "Coding"


print("EXAMPLES")

# 1
print("- - - - -")
print("1")

class Bird:
    can_fly = True
