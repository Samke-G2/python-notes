# Looping over lists                30/01/2025              16:23

# There's an easy way to loop through all the elements of a list by using a 'for' loop.
print("Example 1: using a 'for' loop over a list")
final_score = [17, 22, 34, 13]

for score in final_score:
    print(score)
    
# The loopwill run for as many elements as there are in the list.
# The variable before 'in' holds the value of the element in the current iteration.
print("-----")

artists = ["chagall", "Lissitzky"]

for artist in artists:
    print(artist)
    print("...")
    
# Examples

# 1
items = ["milk", "tomato", "apple"]

for item in items:
    print(item)
    
# 2
minutes_worked = [123, 100, 99, 67]

for minutes in minutes_worked:
    print(f"Overtime worked: {minutes - 60} minutes")
    
