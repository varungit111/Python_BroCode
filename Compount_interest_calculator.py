# Python compound interest calculator
# principle = 0
# rate = 0
# time = 0
#
# while True:
#     principle = float(input("Enter the principle amount: "))
#     if principle < 0:
#         print("Principle can't be less than zero.")
#     else:
#         break
#
# while True:
#     rate = float(input("Enter the interest rate: "))
#     if rate < 0:
#         print("Interest rate can't be less than zero.")
#     else:
#         break
#
# while True:
#     time = int(input("Enter the time in years: "))
#     if time < 0:
#         print("Time can't be less than zero.")
#     else:
#         break
#
# # Calculate compound interest
# total = principle * pow((1 + rate / 100), time)
# print(f"Balance after {time} year(s): ${total:.2f}")



# while True:
#     user_input = input("Enter a number (or 'q' to quit): ")
#     if user_input == 'q':
#         print("Quitting the loop.")
#         break  # Exits the loop
#     else:
#         print(f"You entered: {user_input}")
print("----------------------------------------")

# correct_password = "letmein"
# user_input = ""
#
# while user_input != correct_password:
#     user_input = input("Enter your password: ")
#
# print("Access granted!")
print("----------------------------------------")

# correct_pin = "1234"
#
# entered_pin = input("Enter the PIN: ")
#
# while entered_pin != correct_pin:
#     print("Your PIN is incorrect.")
#     entered_pin = input("Enter the PIN again: ")
#
# print("Correct PIN!")
print("----------------------------------------")
# counter = 0
# while True:
#     print(int(input("enter the {counter}: ")))
#
#     counter += 1
#     if counter >= 9:
#         break
print("----------------------------------------")
correct_pin = "1234"
while True:
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        print("Access granted. Welcome!")
        break
    else:
        print("Incorrect PIN. Try again.")







