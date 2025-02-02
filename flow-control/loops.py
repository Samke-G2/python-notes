# Loops                     25/01/2025                   21:24

# WHILE LOOPS
# Programs repeat the same lines of code over and over again to build all sorts of things.

# One way to repeat lines of code is to write them over and over again, but it takes a really long time if we want to create larger programs.
print("and again")
print("and again")
print("and again")
print("and again")
print("and again")

# To build larger programs and websites, we repeat lines of code using a while loop

counter = 0
print("while loop example")

while counter <= 5:
    print("and again")
    print(counter)
    counter += 1

# A while loop repeats its code block while its conditon is true. 
# The code that the loop repeats comes after the colon :  , inside the indented code block. 
# If a while loop's condition stays True forever, we call it an infinite loop since it will loop infinitely...

# If a while loop's condition is false, the code block will be skipped.
while False:
    print("This will be skipped")



# Stopping while loops              28/01/2025              19:36


# To stop a while loop, we start by creating a variable outside of the loop, 
# We then use the variable in the condition to decide whether or not the loop should run its code block.
# Inside the code block, we stop the loop by updating the varaible until the condition is false.
keep_going = True

while keep_going == True:
    print("One time!")
    
    keep_going = False
    

# The loop runs its entire code block because keep_going is True at first, but doesn't run again after we update keep_going to false.
keep_going = True

while keep_going == True:
    print ("and again")
    
    keep_going = False
    
    print("one more time")
    
    
    

# Controlling While loops               28/01/2025              20:09

# This is how to control the number of times a while loop repeats itself.

# To control the number of times a while loop repeats, we start with a variable set to a number.
# We call this a COUNTER variable.
# Next, we use a comparison in the condition to compare the counter variable to a number.
# Inside the code block, we make the condition return false after a certain number of iterations of the loop in order to stop it.
# The number of loop iterations is controlled by incrementing or decrementing the counter variable.
counter = 1

while counter < 4:
    print(counter)
    counter += 1
print("Go!")


# Changing the condition tells the loop when to stop. For example, changing the condition to counter < 10
counter = 1

while counter <= 10:
    print(counter)
    counter += 1

# changing the counter varaible's value changes when the loop starts.
counter = 5

while counter < 10:
    print(counter)
    counter += 1
    
# The order of your code affects what the console displays. 
counter = 5

while counter < 10:
    counter += 1
    print(counter)
    
    
# Example: 

# 1
first_counter = 0

while first_counter < 5:
    print("**********---------")
    first_counter += 1
    
second_counter = 0

while second_counter < 4:
    print("-------------------")
    second_counter += 1
    
    
    

# FOR LOOPS                 28/01/2025                  20:29

# We know how to repeat code using a while loop, like the emrican flag example.
# Using a while loop, we can write programs with much less code and make it easier for other devs to understand.

for i in range(4):
    print("**********---------")
    
for i in range(4):
    print("-------------------")
    
    
# To create a for loop, we start with the keyword 'for', then a variable like 'i', the word 'in' and finally a range()
# The range statement allows us to specify exactly how many times we want the loop to run.
for i in range(5):
    print("Happy birthday to you!")
    

# Adding a number like 6 inside range() means it'll loop over the code block 6 times, from 0 to 5.
for i in range(6):
    print(i)
    

# The variable, in this case 'i', is the counter variable. It counts that iteration (repetition) of the loop we're currently on.
for i in range(3):
    print(f"We are on loop number {i}")
    
