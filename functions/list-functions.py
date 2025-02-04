# Functions with lists                  04/02/2024                  18:16

# Any type of value can serve as a function's input or output.
print("Opening Example: A function dealing with a list")

def is_multiplayer(players):
    print(len(players) == 2)
    
players = ["Amy", "Jay"]
is_multiplayer(players)