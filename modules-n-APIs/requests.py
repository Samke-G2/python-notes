# Introduction to requests                  17/04/2025                      16:59

# In software development, interacting with web services is a common task, often involving sending requests to servers.
# The Python library 'requests' simplifies the process of making requests
import requests


# The requests library in Python is used for making HTTP requests to a specified URL
# The requests library will make it simple whether you're trying to access a website's data or interact with a web service.

url = "https://rickandmorty.mimo.dev/api/character/1"
response = requests.get(url)
character_data = response.json()

print(f"Name: {character_data["name"]}")
print(f"Status: {character_data['status']}")


# To use requests we have to import it using the 'import' keyword, followed by the package name 'requests'
# We then can call requests.get() and pass it a URL to make an HTTP GET request
# HTTP GET requests are the most common type of request used on the web, primarily designed to retrieve data from a given resource

url = "https://rickandmorty.mimo.dev/api/character/1"
response = requests.get(url)


# The get() function returns a response we can save in a variable
# The response object has a status code and data or an errror attached.
print(response)


# To get to the data, we need to parse the response object.
# We do that with .json()

# The parsed data is a dictionary of keys and values.

data = response.json()
print(data)


# We can access the values as with any other dictionary we work with
print(data["name"])
print(data["status"])


# PART 2                                                            17:17

# Working with web APIs involves sending and receiving data over the internet.
# When working with the response, we need to ensure the integrity of the data.
# That's what the status code is used for.

url = "https://pokedex.mimo.dev/api/pokemon/pikachu"

response = requests.get(url)

if response.status_code == 200:
    print("Data successfully retrieved")
else:
    print("Failed to retrieve data")
    

# The response object has a status_code attached to it
# We should check if it is equal to 200 to ensure the data was retrieved successfully
# After ensuring the data was retrieved successfully, we can unpack it.

if response.status_code == 200:
    print("Data successfully retrieved")

    pokemon_data = response.json()
    print(f"Name: {pokemon_data["name"]}")
    print(f"ID: {pokemon_data["id"]}")
else:
    print("Failed to retrieve data")
    

# Instead of comparing the status code directly, we can also put the request call into a try block.
# We then add an except block to catch potential errors.
# Here, we take the error from the error object and use it as error.

# We should call 'raise_for_status' on the response object to identify errors that we can then catch via the except block.

try:
    response = requests.get(url)
    response.raise_for_status()
    print("Data successfully retrieved")
    pokemon_data = response.json()
    print(f"Name: {pokemon_data['name']}")
    print(f"ID: {pokemon_data['id']}")
except requests.HTTPError as error:
    print(error)






