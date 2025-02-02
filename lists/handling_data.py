# Sorting Data               30/01/2025                 17:22


# Sorted lists are useful when we want to understand where individual data points stand in relation to the others.
scores = [10, 11, 4, 15, 11, 7]

# To sort a list we code teh list name, a dot . , and then sort()
scores.sort()
print(scores)

# Sorting changes the list, so when we reuse or display the list, it will appear sorted.
# When using sort() on a list of numbers, the numbers are sorted in ascending order.

# Lists that have both float values like 9.99 and integers are also sorted based on their numeric values.
prices = [13, 9.99, 10, 7.5]
prices.sort()

print(prices)

# When using sort() on a list of positive and negative numbers, the smallest number (on the number line) goes first.
temperatures = [-1, -3, 2, 0, 5, 3, -4]
temperatures.sort()

print(temperatures)

# When using sort() on a list of strings, the elements get sorted in alphabetical order.
names = ["Charlie", "Alpha", "Beta"]
names.sort()

print(names)



# Summing Data              31/01/2025                      16:31


# Knowing the sum of numbers ina list is useful when comparing different datasets.
signups_june = [30, 6, 20, 12]
signups_july = [20, 5, 100, 40]

# To calculate the total of a list, we use sum() with the list name between teh parentheses.

signups = [30, 6, 20, 12]
print(sum(signups))

# When a list also contains negative numbers, the negative numbers are subtracted from the sum of the positive numbers.
quarterly_growth = [-3, 0, 0, 4]
print(sum(quarterly_growth))

# To reuse the sum of a list, we can store the result in a variable.
scores = [3, 6, 1, 12]
total = sum(scores)
print(total)


# Examples

# 1
june_signs = sum(signups_june)
july_signs = sum(signups_july)

new_signups = july_signs - june_signs
print(new_signups)

# 2
cart = [30, 6, 50]
print(sum(cart))



# Joining Lists             31/01/2025                          16:43

# We'll often encounter different datasets that we should combine into one.
sales_sat = [50, 3, 20, 22, 5]
sales_sun = [60, 10, 9, 11, 40]

# To combine two datasets, weuse the lists' names snd the + operator
print(sales_sat + sales_sun)

# When using + , the second list is appended at the end of the first list
dataset_1 = [1, 2, 3]
dataset_2 = [4, 5]

print(dataset_1 + dataset_2)


# We can also use + to combine lists containing different types of values
seats = [1, 2, 3]
taken = [True, True, False]

print(seats + taken)


# To reuse the combined list, we can save it in a variable
combined = dataset_1 + dataset_2
print(combined)


# Examples

# 1
growth_rate_1 = [0.5, 0.7, 0.8]
growth_rate_2 = [0.8, 0.6, 0.6]

print(growth_rate_1 + growth_rate_2)


#  2
customers = ["Jess", "Mike", "Lynn"]
order_number = [3, 1, 2]

print(customers + order_number)


# 3
team_1 = ["Ana", 78, "Joe", 80]
team_2 = ["Kim", 57, "Sam", 60]

print(team_1 + team_2)



# Counting Elements                 31/01/16:57                 16:57

# When exploring datasets, its good to know how many times a piece of data is present, such as the most frequent answer in a survey
answers = ["yes", "no", "sometimes", "yes", "no"]

# To count how often a value appears in a list, we start with the list name, a dot . , and then count()
# answers.count()

# The value of the element we want to count goes in between the parentheses
print(answers.count("yes"))

# We can use count() with any type of value
free_seats = [False, False, True, True, False]
print(free_seats.count(True))

# To reuse the count of a value in a list, we can store it in a variable
seats_count = free_seats.count(True)
print(seats_count)

# If we don't want to know the exact number, but only if an element appears in a list, we use the keyword 'in'
ingredients = ["flour", "butter", "sugar", "eggs"]
print("sugar" in ingredients)

# Checking if an element is in a list gives us a boolean, either 'True' of 'False'
print("chocolate" in ingredients)

# We can reuse the returned boolean by storing it ina variable 
has_sugar = "sugar" in ingredients
print(has_sugar)


# Example

# 1
missions = ["Moon", "Mars", "ISS", "Mars"]
print(missions.count("Mars"))

# 2
flavours = ["vanilla", "chocolate", "strawberry", "vanilla", "vanilla"]
print(flavours.count("vanilla"))

# 3
winning_numbers = [2, 36, 40, 13]
print(13 in winning_numbers) 





