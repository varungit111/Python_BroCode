# Variable- A container for a value (string,integer, float, boolean)
# A variable behave as if it was the value it contains

#strings - contain word and numbers in " "
first_name= "varun"
food= "pizza"
email = "varun.kumar11120@gmail.com"

print(f"hello {first_name} ")
print(f"you like {food}")
print(f"your email address: {email}")

#integers - numbers only
age =25
quantity= 3
num_of_student=30
print (f"you are {age} years old")
print(f"you are buying {quantity} items")
print(f"your class has {num_of_student} students")

#float - decimal numbers

price =10.99
gpa=3.2
distance = 5.9
print(f"This curry will cost you {price}")
print(f"your gpa is {gpa}")
print(f"you ran {distance} kilometers")

#Boolean
is_student = True
print(f"Are you a student? : {is_student}")

is_student = True
if is_student:
    print("You are a student")
else:
    print("you are not a student")

is_online = True
if is_online:
    print("you are online")
else:
    print("you are offline")





