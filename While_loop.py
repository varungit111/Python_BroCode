# while loop = execute some code WHILE some conditions remain true
# name= input("Enter your name: ")
#
# while name == "":
#     print("you did not enter your name")
#     name = input("Enter your name: ")
#
# print(f"Hello {name}")
print("----------------------------------------------")

# age= int(input("Enter your age: "))
#
# while age<=0:
#     print("age can't be negative")
#     age = int(input("Enter your age: "))
# print(f" you are {age} years old")

print("----------------------------------------------")
# food= input("Enter a food you like(q to quit): ")
#
# while not food =="q":
#     print (f"you like {food}")
#     food = input("Enter a food you like(q to quit): ")
#
# print("bye")
print("----------------------------------------------")

num=int(input("Enter a number between 1 to 10: "))
while num<1 or num>10:
    print(f"{num} is invalid")
    num = int(input("Enter a number between 1 to 10: "))
print(f"your number is {num}")


