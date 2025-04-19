# format specifiers = {value:flags} format a value based on what flags are inserted

price1=234.23456
price2= -2345.96423
price3=234.086

# print(f"price 1 is ${price1: .2f}")
# print(f"price 2 is ${price2: .2f}")
# print(f"price 3 is ${price3: .2f}")

# print(f"price 1 is ${price1: >10}")
# print(f"price 2 is ${price2: <10}")
# print(f"price 3 is ${price3: ^10}")

# print(f"price 1 is ${price1:+}")
# print(f"price 2 is ${price2:+}")
# print(f"price 3 is ${price3:+}")

print(f"price 1 is ${price1:+,.2f}")
print(f"price 2 is ${price2:+,.2f}")
print(f"price 3 is ${price3:+,.2f}")