# Errors and exceptions (PART 1)                    19/02/2025                          16:00


# SyntaxError

# Sometimes Python is unable to understand our code. 
# This results in something called a SyntaxError

# Syntax errors are usually due to typos, such as mispelled keywords.
# Incorrect or missing indentation will result in an IndentationError, which is a specific type of SyntaxError
# Putting a keyword in the wrong place will also cause a SyntaxError
# Leaving out symbols, such as colons and brackets, will also cause a SyntaxError
# If we try to run incomplete statements we'll also receive a SyntaxError

# Sometimes Python can add more detail to the error, like where a string is mistakenly used as a variable name.

# The ^ symbols, known as a caret, indicates in the console where the error has been found in the code



# Errors and exceptions (PART 2)                 19/02/2025                         16:13

# Something Python understands our code, but cannot executes it.
# Python will raise an EXCEPTION when it cannot perform an operation.
# The text shown in the console when an exception is raised is called the traceback. It helps us DEBUG our code, which means finding errors.

# ZeroDivisionError, NameError and TypeError are examples of different types of exceptions.

# We'll encounter many types of exceptions when creating programs, relating to things such as indexing, file reference, variables
# If we try to use a variable that doesn't exist, we'll get an error -- a NameError
# Objects may not have attributes or methods that we think they have.

# Some methods don't produce errors and are able to handle issues themselves.



# Errors and Exceptions (Part 3)                  19/02/2025                         16:23

# The traceback is best read from bottom to top, to understand what went wrong with our code.
# If Python cannot find a module, a ModuleNotFoundError exception will be raised.
# If an index is out of range, an IndentationError exception will be raised

# Syntax errors are returned before Python attempts to run the code
# a NameError exception is raised only after the SyntaxError later in the code had been fixed
# Error messages help us Debug our code when it's not behaving the way we expect it to behave.


# A logic error occurs when there is no error or exception, but our code does not work correctly





