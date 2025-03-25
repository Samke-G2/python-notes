# Filtering with 'if' statements                13/03/2025                  22:41

# We can use list comprehensions to create a new list by filtering elements of an existing one
print(" ")
print("Example 1: filtering an existing list ")

scores = [12, 47, 30, 29, 19, 35]

high_scores = [score for score in scores if score > 20]

print(high_scores)
# We start out like usual, with the 'for' loop, 
# To copy each score element in our new list, we write 'score' as our expression, without applying any operations
# To filter for elements that meet a certain condition, we add an 'if' statement, whihc adds only the elemetns that meet that condition

# When using a conditional, the usual order is starting with the expression, followed by the 'for' loop, and ending with the 'if' statement.
print(" ")
print("Example 2: Using a conditional ")

prices = [150, 45, 200, 340]

apply_taxes = [price for price in prices if price > 150]

print(apply_taxes)


print(" ")
print("EXAMPLES")

# 1
print("- - - - - ")
print("1 ")

item_prices = [120, 25, 40]

under_50 = [price for price in item_prices if price < 50]

print(under_50)

# 2
print("- - - - - ")
print("2 ")

humidity = [40, 35, 20, 70]

too_low = [level for level in humidity if level < 30]

print(too_low)

# 3
print(" - - - - -")
print("3 ")

websites = ["nytimes.com", "lemondes.fr", "economist.co.za"]

french = [website for website in websites if website.count(".fr") > 0]

print(french)

# 4
print("- - - - - ")
print("4 ")

humidity_percent = [40, 35, 20, 70]

ideal = [level for level in humidity_percent if level >= 30 and level <= 50]

print(ideal)

# 5
print("- - - - - ")
print("5 ")

book_codes = ["FH2010", "BV1999", "LB2010"]

book_2010 = [code for code in book_codes if code.count("2010") == 1]

print(book_2010)
