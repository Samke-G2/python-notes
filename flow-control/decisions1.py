# Making decisions 1        24/01/2025       16:35

intro1 = "Smart programs use booleans to make decisions on whether to run lines of code or skip them."
intro2 = "We use an 'if' statement to write code that responds to different situations."
intro3 = "We recognise it by the keyword 'if'."
print(intro1)
print(intro2)
print(intro3)

if True:
    print("Hello!")
    
para1 = "The 'if' statement runs code only if it is evaluated as true. It's like saying, 'if' something is true, then do this."
para2 = "But what if we want to skip the code? In that case, we need the statement to evaluate as false."
print(para1)
print(para2)

if False:
    print("Hello!")

para3 = "Values like 'True' are called 'conditions'. Statements relying on conditions are called 'conditionals'."
para4 = "Conditions decide if the code runs or gets skipped, they come in between 'if' and the colon ':'."
print(para3)
print(para4)


# Making decisions 2        24/01/2025          16:52

intro_p2 = "'if' statements don't decide on skipping or running the entire code. They only make decisions about a code block."
print(intro_p2)

if True:
    print("I'm a code block!")
    
para1_p2 = "We use an indentation (of of 4 spaces, or 'tab') to highlight code blocks. Indentation refers to the space between the code and the code editior's margin."
para2_p2 = "A code block can be more than a one-liner. All lines with the same indentation belong to the same code block."
print(para1_p2)
print(para2_p2)

if True:
    print("Look at me!")
    print("I am a code block!")
    
para3_p2 = "If the indentation is incorrect, the computer can't understand your code. This leads to an 'IndentationError' showing up in the console."

para4_p2 = "Instead of using the boolean 'True', we can save it in a variable like 'greet' and use it as the condition."
print(para4_p2)

greet = True
if greet:
    print("Hello!")

para5_p2 = "Using a variable set to 'false' allows us to skip code like the display statement."
greet = False
if greet:
    print("Hello!")

q1 = "What do we call the code that is indented after an 'if' statement?"

# q2 = 