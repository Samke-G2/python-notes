# Returning Tuples                      06/02/2025                      17:47

# Tuples are useful because they allow us to return multiple values from a function, like the highest and lowest scores from a list
def get_score_data(score_list):
    highest_score = max(score_list)
    lowest_score = min(score_list)
    
    return highest_score, lowest_score

# To return a tuple, we code the values that we wish to return separated by a comma
# Even though we're returning a tuple, parentheses are not necessary.
# To store a tuple returned by a function, we assign the function call's result to a variable
print("Example 1: Storing a returned tuple in a variable")

scores = [32, 17, 80]
extremes = get_score_data(scores)

print(extremes)


# We can retrieve the individual values by their indeces
print("    ")
print("Example 2: Accessing the returned tuple values with their indeces")

highest = extremes[0]
lowest = extremes[1]
print(f"lowest score: {lowest}")
print(f"highest score: {highest}")


# Since tuples are immutable, we return a tuple when we won't need to modify it, but just use the values 
print("    ")
print("Example 3: Using the values returned from an immutable tuple")

def get_top_three(players):
    return players[0], players[1], players[2]

players = ["Sue", "Ed", "Ann", "Ty"]

top_three = get_top_three(players)

print(f"First: {top_three[0]}")
print(f"Second: {top_three[1]}")
print(f"Third: {top_three[2]}")


# When we want to be able to modify the returned collection of values, we return a list
print("    ")
print("Example 4: Returning a collection we can modify (a list)")

def form_team(players):
    team = []
    team.append(players[0])
    team.append(players[2])
    return team

team = form_team(players)

team[0] = "chloe"
print(team)


# Examples 
print("- - - - -")
print("EXAMPLES")

# 1
print("- - - - -")
print("1")

def check_age(age):
    can_drive = age >= 18
    return age, can_drive

print(check_age(26))
print(check_age(17))

# 2
print(" - - - - -")
print("2")

def analyze_profit(gains, expenses):
    profit = gains - expenses
    after_taxes = 0.85