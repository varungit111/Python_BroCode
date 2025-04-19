#print(help(str)) # to check all the string methods


# name = input("Enter your full name: ")
# phno= input("enter your phone number: ")
# result = len(name)
# result= name.find("V")
# result= name.rfind("a")
# result= name.capitalize()
# result= name.upper()
# result= name.lower()
# result= name.isdigit()
# result= name.isalpha()
# result=phno.count("-")
# result=name.replace("v", "k")
# print(result)

username=input("Enter a username: ")
if len(username)>12:
    print("your username can't be more than 12 characters")
elif not username.find(" ") ==-1:
    print("your username can't contain spaces")
else:
    print(f"welcome{username}")
