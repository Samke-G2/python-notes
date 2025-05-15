# Constructors                          # 12/05/2025                            # 16:03

# There's a method we can use that is more flexible when creating different instances from a class
# It's called the CONSTRUCTOR method
print(" ")
print("Example 1: Intro to constructor method")

class Virtual_Pet:
    def __init__(self, color):
        self.color = color
        
rocky = Virtual_Pet("brown")
benny = Virtual_Pet("black")

print("Rocky and Benny are both virtual pets.")
print(f"Rocky is: {rocky.color}")
print(f"Benny is: {benny.color}")


# The constructor method looks like : _ _init_ _() : and allows us to set unique values for the class variables when we create an instance.
# Make sure to use the double underscore on each side of init

# When we create an instance from the class definition, we're able to pass unique values inside the parentheses

chirpy = Virtual_Pet("yellow")

# Just like with regular class methods, we need to add 'self' as the first parameter to the constructor method.
# Next, we add the parameters for the custom values we want to set when we create the instances
# Then we set the value by coding self, a . , the parameter name, and then equating the parameter name again
# When we create an instance from the class definition, we add the values we want to set inside the parentheses.
print(" ")
print("Example 2: Setting custom values with the constructor method ")

clifford = Virtual_Pet("red")

print(f"Clifford the big {clifford.color} dog.")


# The constructor method helps us construct the instances of our class the way we want.
# We're able to add as many parameters as we want.
print(" ")
print("Example 3: Adding more parameters ")

class Virt_Pet:
    def __init__(self, color, legs, type):
        self.color = color
        self.legs = legs
        self.type = type
        
spike = Virt_Pet("black", 4, "dog")

print(f"Spike is a {spike.color} {spike.type} with {spike.legs} legs.")
# We can access the parameters from other places in the class definition by using 'self.'


class Pokemon2:
    def __init__(self, color, name):
        self.color = color
        self.name = name
        
charizard = Pokemon2("orange", "Charizard")
print(charizard.color)
print(charizard.name)










