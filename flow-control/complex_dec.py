# Using complex decisions               25/01/2025              13:48


# We know how to run or skip code based on a condition:
age = 17
has_permit = True

if age > 16:
    print("Can drive")
    

# What if we wanted to run or skip code depending on two conditions?

if age > 16 and has_permit:
    print("Can drive")
    

# The 'and' operator allows us to run code only if both conditions are true.
# It skips the code block if one or more conditions are false,

if age > 18 and has_permit:
    print("Can drive")
    
    
# We can add as many conditions as we want.
is_insured = True

if age > 16 and has_permit and is_insured:
    print("Should be driving")
    
    
    
# Part 2                    25/01/2025                          14:00


# We use the 'or' operator for alternate conditions, like enabling something if at least one condition is met.
# To run code when either one of the conditions is "True", we use the 'or' operator
average_grade = "A"
final_score = 1400

if average_grade == "A" or final_score >= 1500:
    print("Certificate achieved!")
    
# With 'or', gets skipped only if all conditions are False

# We can use 'or' to add as many conditions as we want.
average_grade = "B"
final_score = 1400
won_competition = True

if average_grade == "A" or final_score >= 1500 or won_competition:
    print("Certificate achieved!")
    
    
# Examples

# 1
is_summer = False
is_warm = True

if is_summer or is_warm:
    print("Go for a swim")
    
    
# 2
is_weekend = False
on_vacation = True

if is_weekend or on_vacation:
    print("Go on a roadtrip")
    
    
# 3
promote_article = False
views = 100
shares = 30
likes = 70

if views > 150 or shares >= 50 or likes >= 60:
    promote_article = True
    
    
