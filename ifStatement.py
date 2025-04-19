# if statement = Do some code only if some condition is true
#     else do something else

# age=int(input("enter your age"))
# if age>=100:
#     print("you are too old to sign up")
# elif age<=0:
#     print("you haven't been born yet")
# elif age>=18:
#     print("you are signed up now")
# else:
#     print("you must be 18+ to sign up")

name= input("Enter your name: ")
if name =="":
    print("you did not type your name")
else:
    print(f"Hello {name}")

print("----------------------------------------------------------------")

online = True
if online:
    print("the user is online")
else:
    print("the user is offline ")



