# Understanding Classes                         15/05/2025                      16:28

# Similar to naming variables and functions, there are some common practices when defining classes
# Class names usually have the first letter capitalized and the rest lowercase.
# Like variables, we try to name classes descriptively.
# As with naming variables and functions, we should name things consistently and watch out for capitalisation.
print(" ")
print("Example 1: Class naming practices")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sayHello(self):
        print(" Hello ")
        
    def sayBye(self):
        print(" Bye ")

teacher = Person("Emily", 24)
teacher.sayBye()

class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
        
mistborn = Book("Brandon Sanderson", "Mistborn")


# Like methods outside classes, we can use Python's built-in functions and core features.
print(" ")
print("Example 2: Using built-in functions in a class")
class Pie:
    def __init__(self, flavour, ingredients):
        self.flavour = flavour
        self.ingredients = ingredients
        
    def print_ingredients(self):
        for i in self.ingredients:
            print(i)
            
applePie = Pie("apple", ["flour", "eggs", "apples", "butter"])
applePie.print_ingredients()


print("EXAMPLES")

# 1
print("- - - - - ")
print("1")

class Bookseries:
    def __init__(self, name, books):
        self.name = name
        self.books = books
        self.num_books = len(books)
        
    def displayBooks(self):
        for i in self.books:
            print(i)
            
    
            
            
hunger_games = ["The Hunger Games", "Catching Fire", "Mockingjay"]

hungerGames = Bookseries("The Hunger Games", hunger_games)
hungerGames.displayBooks()
print(f"The series has {hungerGames.num_books} books")


# 2
print("- - - - - ")
print("2")

class Contact:
    first = "Jane"
    last = "Doe"
    cell = "311 244 5656"
    email = "jdoe@gmail.com"
    
    






