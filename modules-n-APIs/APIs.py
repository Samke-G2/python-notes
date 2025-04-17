import requests

# Communicating with an API (Part 1)              20/02/2025                            21:48

# Application Programming Interfaces, also known as API, facilitate communication between two programs.
# APIs send requests from a sender program to a receiver program.
# Then they send responses from the receiver to the sender program.

# Many things in our daily life work like an API.
# One example is a waiter and the kitchen staff.
    # A waiter, like a sender program, sends an order to the kitchen.
    # Then the kitchen, as a receiver program, sends back the food as a response.


# Now, back to programs
# The code below sends a GET request to an API.     Can you guess what a GET request does?
# If everything works,
# we should receive the data along with a status code of 200, telling us everything went OK.
print("       ")
print("Example 1.1: Using a GET request")

# GET https://mimo.org/courses HTTP/1.1     <<  This one is an outdated method, and it the url returne 404
example = requests.get("https://w3schools.com", timeout=2.50)
print(example.status_code)


# The code was for us to request some data
# https://w3schools.com is the API that helped us get it

# Where did the API get the information from?
# The API connects with another program to retrive information from a database

# To interact with databases, we need to write code. An API allows us to do that in a simpler way.
# The correct method is important when performing these actions
# To retrieve data, we use GET
# To insert data we use POST

# We can insert data into a database using the POST request.
# Unlike with GET, we need to send a body with the information for POST requests
print("       ")
print("Example 1.2: Using a POST request")

# POST https://mimo.org/users HTTP/1.1     must research proper post method when online

data = {
    "username": "test_user",
    "name": "tester"
}


# When working with Python, we use the requests library to create requests
print("       ")
print("Example 1.3: Usig the requests library to make a GET request")

response = requests.get("https://mimo.org/courses", timeout=3.0)
data = response.json()
print(data)


# We can also make POST requests with the requests library.
print("       ")
print("Example 1.4: Using the requests library to make a POST request")

url = "https://mimo.org/users"

response = requests.post(url, json=data, timeout=3.0)
print(response.json())



# Communicating wiht an API (Part 2)            24/02/2025                      16:57

# Now that you know what an API is, why should we use it?
# One reason is that APIs can help us build a system quicker.

# Back-end developers (devs) don't need to wait for front-end development to be completed to test their program.
# They can test their program by simply sending requests to the API and checking if the responses are correct.


# We've gone through GET, and POST requests
# There are also DELETE, PUT, and PATCH requests to learn about.

# DELETE requests must have an identifier to let the API know what to delete.
print("       ")
print("Example 2.1: Using a DELETE request.")

# DELETE https://mimo.org/api/courses/6
# HTTP/1.1

# We use the delete method to call a delete endpoint using requests
url2 = "https://mimo.org/api/courses/1"

response = requests.delete(url2, timeout=3.0)


# PUT requests are similar to POST requests, but are used to replace an object previously created.
# Since PUT requests are used to replace existing objects, they need identification to know which object to replace
print("       ")
print("Example 2.2: Using a PUT request")

# PUT https://mimo.org/users/1 HTTP/1.1

# {
#     "username": "test_user",
#     "name": "tester"
# }

# If an invalid identification, or no identification, is provided in a PUT request
# A new object will be created.

# The status code of a response will be 201 for object created
# and 204 for object replaced

# When using a PUT request, it removes all existing data and inserts the data based on the body of the request.

# We use the put() method to call a put endpoint using requests

data2 = {
    "username": "New name",
    "userId": 1
}

response = requests.put(url2, json=data, timeout=3.0)


# PATCH requests are used to update some fields of an object so identification is neede to determine which object to update.
# Values of all unmentioned fields will remain unchanged

# We use the patch() method to call a patch endpoint using requests
print("       ")
print("Example 2.3: Using the PATCH method")

data2 = {
    "completed": True
}

response2 = requests.patch(url, json=data, timeout=3.0)


print("EXAMPLES")

# 1
print("- - - - -")
print("1")

# write the Python code to send a DELETE request to remove the lesson with the identification 1001
response = requests.delete("https://mimo.org/lesson/1001")
print(response.status_code)

# 2
print(" ")
print("2")

# write the code to send a PUT request using Python to replace the user with the identification 17
# the user's name should be changed to Bob and the username should be changed to bobbyman

url = "https://mimo.org/users/17"
data = {
    "username": "bobbyman", 
    "name": "Bob"
}

response = requests.put(url, json = data)
print(response.status_code)

