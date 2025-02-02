# Using Conditions          24/01/2025          17:43

intro = "There's a trivia app that displays 'Correct!' if we submit the correct answer and 'Not quite!' if we pick the wrong answer."
intro2 = "To make decisions like these in our programs, we need 'if' statements that rely on conditions."
print(intro)
print(intro2)

para1 = "We can use comparison operators in programs like the Trivia app to check if the answer to a question is correct."
print(para1)

answer = "Picasso"
if answer == "Picasso":
    print(answer + " is correct!")
    
para2 = "What if the trivia quiz answer isn't correct? We can use the inequality operator != to check if 'answer' is not equal to 'Picasso'."

answer2 = "Matisse"
if answer2 != "Picasso":
    print(answer2 + " is wrong!")
    
# 'if' statements work with all comparison operators we've explored so far.
# Like checking if age is greater than or equal to 55
age = 75
if age >= 55:
    print("Discount applied")
    
# Or using == to compare variables like is_day to boolean values
is_day = True
if is_day == True:
    print("Lights off!")
    
# We can store the result of a comparison in a variable.
score = 51
pass_grade = score > 50
if pass_grade:
    print("Passed!")
    
# Examples:

# 1
song = "Don't stop me now"
replay_times = 345

if replay_times >= 300:
    print("Your top song this week: ")
    print(song)
    
# 2
today = "Sunday"
if today != "Saturday":
    print("Set alarm at 8:00")
    



# Coding Else statements            24/01/2025          18:03


# Great software doesn't just decide what to do when a condition is True, it also has a back-up plan if the condition is False
# Like an app that switches the lights on if is_on is True and off if is_on is False.

# This if statement uses the 'not' operator to run a different code block if the condition is False
available = True

if available:
    print("In stock")
if not available:
    print("Out of stock")
    
# Instead of creating two 'if' statements, we use an if/else statement to achieve the same result.
available = False 

if available:
    print("1 in stock")
else:
    print("Out of stock")
    
# Let's look at a use case: if is_day is True, we want to turn the lights off.
is_day = True

if is_day:
    print("Lights off!")

# The else statement doesn't need its own condition because it handles the cases where the if's condition is Fasle.
number = 99

if number == 1:
    print("It's 1")
else:
    print("It's not 1")
    
# Examples:

# 1
chosen_number = 7

if chosen_number == 12:
    print("You guessed right!")
else:
    print("Have another go")
    
# 2
common_friends = 3

if common_friends > 2:
    print("Friend suggestions: Sue")
else:
    print("No new friend suggestions")
    
# 3
rating = 87

if rating >= 90:
    print("Buy movie tickets")
else:
    print("Homeflix & skip the bill")
    
    
    

# Incorporating Elif                25/01/2025              13:21


# Using 'if' and 'else' statements, we can write a program that shows one greeting if hour is less thn 12 and another if it does not fulfill the condition
hour = 0

if hour < 12:
    print("Good morning")
else:
    print("Good night")
    

# For a more specific condition, like if hour is greater than 12, but less than 17, we can code an elif statement instead
hour = 14

if hour < 12:
    print("Good morning")
elif hour < 17:
    print("Good afternoon")
    
    
# The elif statement runs its code block if the conditions before it were false, and its condition is true.
# We can code an else statement to run its code block when the if and elif conditions are false.
hour = 18

if hour < 12:
    print("Good morning")
elif hour < 17:
    print("Good afternoon")
else:
    print("Good night")
    

# As long as they go before the else statement, we can add as many elif statements as we'd like.
hour = 20

if hour < 12:
    print("Good morning")
elif hour < 17:
    print("Good afternoon")
elif hour < 21:
    print("Good evening")
else:
    print("Good night")
    

# Examples:

# 1

score = 66

if score > 99:
    print("You get an A!")
elif score > 70:
    print("You passed!")
else:
    print("Better luck next time!")
   
    
# 2

age = 16

if age <= 12:
    print("Where are your parents?")
elif age <= 16:
    print("You're too young to ride this ride.")
else:
    print("Welcome")
    
    