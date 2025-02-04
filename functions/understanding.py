# Understanding functions               02/02/2025                  23:00

# Giving functions descriptive names helps us to know at  glance what they do.
print("Opening example")
def get_final_price(price, tax):
    return price + tax

price = get_final_price(30, 1.5)
print(price)


# Functions are actions so their names often start with verbs.
def create_email(name):
    return name + "@hutmail.com"


# Functions that return values are often start with verbs like "get", "compute", or "calculate"
print("     ")
print("Example 1: Functions that return values")

def get_telephone(prefix, number):
    return prefix + number

def calculate_sum(num1, num2):
    return num1 + num2

print(get_telephone("011 ", "752-6050"))
print(calculate_sum(5, 10))


# Functions that return boolean values often start with "is".
print("     ")
print("Example 2: Functions that return boolean values")

def is_freezing(temperature):
    return temperature < 0

print(is_freezing(-5))
print(is_freezing(10))


# The key is to keep the same naming practice for functions that perform a similar task.
print("     ")
print("Example 3: Names for functions that perform similar tasks")

def calculate_product(num1, num2):
    return num1 * num2

print(calculate_product(5, 10))

def calculate_difference(num1, num2):
    return num1 - num2

print(calculate_difference(5, 10))



# Examples
print("     ")
print("EXAMPLES")

# 1
def display_item_price(item, price):
    print(f"{item}: R{price}")
    
display_item_price("chocolate", 13)


# 2
def generate_username(name, b_day):
    return (f"{name}_{b_day}")

user = generate_username("ty", 17)
print(user)


# 3
def get_free_seats(booked, total):
    return total - booked

free = get_free_seats(13, 20)
print(free)


# 4

