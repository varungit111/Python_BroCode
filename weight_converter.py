weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds? (K or L): ")
if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"your weight is: {weight} {unit}")
elif unit == "L":
    weight = weight/2.205
    unit = "kgs"
    print(f"your weight is {weight} {unit}")
else:
    print(f"{unit} is not valid")



