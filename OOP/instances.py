# Creating instances                        24/04/2025                          17:43

# When we want to use our class template to create something, we start by creating a variable.
# Next, we add the class name and parentheses to create it
# When we create variables from the class template, we're creating instances.
print(" ")
print("Example 1: Creating instances")

class VirtualPet:
    color = "brown"
    
fluffy = VirtualPet()
benny = VirtualPet()


# The VirtualPet class used to create the 'fluffy' varable is called the DEFINITION and the variable created is called the INSTANCE
class VirtualPet2:
    color = "brown"
    legs = 4
    lives = "9"
    wagging_tail = True
    
fluffy = VirtualPet2()


# To access a class variable, we add the instance name, a full stop .  , and the name of the variable we want.
print(" ")
print("Example 2: Accessing a class variable")

skippy = VirtualPet2()
print(skippy.legs)

# We can thus access all of the variables we created in the class definition
print(" ")
print("Example 2 continued")

print(skippy.wagging_tail)
print(skippy.color)


print("EXAMPLES") 

# 1
print("- - - - -")
print(" 1")

class Pokemon:
    name = "squirtle"
    weight = 19.8
    color = "blue"
    
pokemon = Pokemon()
print(pokemon.name)
print(pokemon.weight)




