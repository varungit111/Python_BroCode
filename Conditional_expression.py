# conditional expression = A one-line shortcut for the if-else statement(ternary operator)
#                          print o=r assign one of two values based on condition
#                            X if condition else Y

num= 5
a= 6
b=7
age= 13
temperature = 30
user_role ="admin"

print("positive" if num>0 else "Negative")
result = "Even" if num%2 ==0 else "odd"
max_num = a if a>b else b
min_num = a if  a<b else b
status = "Adult" if age>= 18 else "Child"
weather = "HOT" if temperature>30 else "nice weather"
access_level = "Full access" if user_role == "admin" else "limited access"
print(status)
print(max_num)
print(user_role)
