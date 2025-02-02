# Advanced Loop control             28/01/2025                  20:59


# Let's explore using 'continue', 'break', and 'else' to control the loop flow, skip iterations, exit early, or run code after the loop.

# 'continue' is used to skip the current block and move to the next iteration.
print("Example 1")
for i in range(1, 6):
    if i == 2:
        continue
    print(i)
    
print("Example 2")
shopping_list = ["apples", "bananas", "bread", "milk", "chips", "eggs"]

for item in shopping_list:

    if item == "chips" or item == "bread":
        continue
    print(f"Don't forget to buy: {item}")


# The 'break' statement exits the loop entirely. When invoked, the rest of the iteration and sebsequent iterations of the loop will be skipped.
print("Example 3")
for i in range(1, 6):
    if i == 3:
        break
    print(i)
    
# We can use the 'break' keyword to break out of a 'while' loop if a certain condition is met.
print("Example 4")

password = "open sesame"
looping = True

while looping == True:
    if input("Enter the password: ") == password:
        print("Access granted")
        break
    print("Incorrect password. Try again.")
    

# Finally, the 'else' statement in loops is executed when the loop has finished. This differs from the 'else' in in an 'if' statement.
print("Example 5")

for i in range(1, 6):
    print(i)
else: 
    print("Loop has ended")
    
# The 'else' block will only be executed if teh loop is not terminated early by a 'break' statement.
print("Example 6")

for i in range(1, 11):
    if i == 5:
        break
    print(i)
else:
    print("Loop has ended.")
    
    
# Examples:

# 1
shows = ["The office", "Dexter", "Friends"]

for show in shows:
    print(show)
else:
    print("Those are mimo's favourite shows.")
    

# 2
tasks = ["pending", "completed", "pending", "pending"]
index = 0

while index < len(tasks):
    if tasks[index] == "completed":
        print(f"Skipping task {index + 1}.")
        index += 1
        continue
    print(f"Processing task {index + 1}.")
    index += 1

# 3
tasks = ["email boss", "fix bug", "attend meeting"]

for task in tasks:
    if task == "fix bug":
        print("Urgent task found: fix bug")
        break
    print(f"Working on: {task}")
    
# 4
for char in "hello":
    if char == "o":
        break
    print(char)
    
    