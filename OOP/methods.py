# Classes with Methods                      # 08/05/2025                    16:38

# Classes can have functions too, which are known as METHODS when theyre inside of a class.
print(" ")
print("Example 1: Intro to methods")

class Virtual_Pet:
    color = "brown"
    legs = 4
    
    def bark(self):
        print("Woof")
        
    def display_color(self):
        print(self.color)
        
    def display_legs(self):
        print(self.legs)
        
    def sit(self):
        print()
        
rocky = Virtual_Pet()
rocky.bark()
# 'self' is a special keyword that we need to use inside our class definition. 
# We pass 'self' as the first parameter to all the methods we add.

# We use 'self' as a parameter in the class methods so that we can access the class variables inside the methods.
print(" ")
print("Example 2: Using the 'self' keyword")

rocky.display_color()
rocky.display_legs()
# Without using 'self' we wouldn't be able to access thte class variable as they are declared outside of the class method's scope


# To use a class method, it's the same as using a class variable, except we need to add parentheses.
print(" ")
print("Example 3: Using a class method")

rocky.bark()


print("EXAMPLES")

# 1
print("- - - - -")
print("1 ")

class Dog:
    def __init__(self):
        self.color = "brown"
    def print_color(self):
        print(self.color)
        
spot = Dog()
spot.print_color()


# 2
print("- - - - -")
print("2")

class Pokemon:
    name = "Pikachu"
    color = "yellow"
    
    def introduce(self):
        print("Hi")
        print("I am" + self.name)
        
pikachu = Pokemon()
pikachu.introduce()
