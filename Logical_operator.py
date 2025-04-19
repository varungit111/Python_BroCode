# logical operators = evaluate multiple conditions (or, and not)
#                     or = at least one condition must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)

# temp= int (input("Enter the temperature: "))
# is_raining = True
#
# if temp>= 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("the outdoor event is still scheduled")
print("--------------------------------------------------------------")

temp= int (input("Enter the temperature: "))
is_sunny= False

if temp>= 28 and is_sunny:
    print("It is Hot weather 🥵")
    print("It is sunny ☀️")
elif temp<0 and is_sunny:
    print("It is cold outside 🥶")
elif temp>28 and not is_sunny:
    print("It is cloudy ☁️")
else:
    print("It is pleasent weather ❤️")
