# Practice file for list comprehension concepts                 25/03/2025                 17:31

# 1
print("- - - - - -")
print(" 1 ")

passwords = ["012345", "Xhf!%m0&&"]

def is_valid(password):
    percent = password.count("%") > 0
    and_sign = password.count("&") > 0
    return percent or and_sign

valid = [is_valid(password) for password in passwords]
print(valid)


# 2
print("- - - - - -")
print(" 2 ")

networks = ["open-WIFI", "guest", "Wi-Fly"]

open_networks = [wifi for wifi in networks if wifi.count("open") > 0]


# 3
print("- - - - - -")
print(" 3 ")

distance = [1, 4, 20, 14]

walking_distance = [km for km in distance if km <= 5]
print(walking_distance)


# 4
print("- - - - - -")
print(" 4 ")

numbers = ["+43 5753335", "+44 0051239", "+27 737526050", "+27 832107865", "+33 1218817"]

sa_numbers = [num for num in numbers if num.count("+27") == 1]
print(sa_numbers)


# Final
print("-------------")
print("Final one that I created ")

songs = ["Ngiyazifela", "Lay me down (feat. John Legend)", "Now N Then", "Save You", "Run (feat. Lady leshurr)", "Ngud' (feat. Hosh karamaima)"]
features = [song for song in songs if song.count("(" and ")") != 0]
print(features)
