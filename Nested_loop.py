# nested loop = A loop within another loop (outer, inner)
# outer loop:
#inner loop:

for x in range(4):
    for y in range(1, 10):
        print(y, end="")
    print()
print("-----------------------------------------------")

rows= int(input("enter the number of rows: "))
columns= int(input("enter the number of columns: "))
symbol= input("enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
