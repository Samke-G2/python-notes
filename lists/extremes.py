# Finding Extreme Data              30/01/2025              17:08

# To explore the data we store in lists, its often useful to find teh extreme values: the minimum and the maximum.
scores = [3, 6, 1, 12]
print(scores)

# To find the largest number in a list of data, code max() with the name of the list between parentheses.
print("Maximum: ")
print(max(scores))


# To find the smallest number in a list, we use min() with the list name between parentheses
print("Minimum: ")
print(min(scores))


# We can reuse the results of min() and max() by saving them in variables
min_score = min(scores)
max_score = max(scores)

print(f"The smallest value is: {max_score}.")
print(f"The largest value is: {min_score}.")


# Examples:

# 1
jean_sizes = [25, 28, 40]
largest = max(jean_sizes)

# 2
weekly_profits = [50, 60, 70, 20]
max_profit = max(weekly_profits)

print(max_profit)

# 3
