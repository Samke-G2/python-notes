# Functions with lists                  04/02/2024                  18:16

# Any type of value can serve as a function's input or output.
print("Opening Example: A function dealing with a list")

def is_multiplayer(players):
    print(len(players) == 2)
    
players = ["Amy", "Jay"]
is_multiplayer(players)


# We pass lists to functions just like we do any other value: by coding the list name between the function's parentheses
print("     ")
print("Example 1: Passing a list as function's parameter")

def display_programme(movies):
    print(f"Airing tonight: {movies}")
    
movie_list = ["Alien", "Moon"]
display_programme(movie_list)

# Once we pass the list to the function, we can use the parameter to display it
# Remember that parameters are like variables storing the values we pass to a function.


# Inside the function, we can use all teh list operations we've learned so far.
print("     ")
print("Example 2: Using list operations in functions - len() ")

def count_passengers(passengers):
    print(f"There are: {len(passengers)} passengers aboard.")
    
passengers = ["June", "Sam", "Lee"]
count_passengers(passengers)

# Sometimes we'll want our function to retrieve certain elements of a list
print("     ")
print("Example 3: Indexing a list")

def get_winner(top_players):
    winner = top_players[0]
    print(f"Game winner: {winner}")
    
top_players = ["Jay", "Meg", "Cy"]
get_winner(top_players)


# Functions can also update lists
print("     ")
print("Example 4: Updating a list ")

def update_first_place(leaderboard, player):
    leaderboard[0] = player
    return leaderboard

leaderboard = ["Jay", "Meg", "Cy"]
leaderboard = update_first_place(leaderboard, "Lena")
print(leaderboard)



# EXAMPLES
print("     ")
print("EXAMPLES")

# 1
print("- - - - - - - -")
print("1")

def get_middle_name(names):
    return names[1]

name_list = ["Thomas", "Stearns", "Elliot"]
ts_eliot = get_middle_name(name_list)
print(ts_eliot)

# 2
print("- - - - - - - -")
print("2")

def is_discounted(basket):
    print(len(basket) >= 2)
    
basket_items = ["t-shirt", "jeans", "jeans"]
is_discounted(basket_items)

