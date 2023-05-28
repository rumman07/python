#Minimum
smallest = int(input("Enter a value: "))
inputStr = input("Enter a value: ")
while inputStr != "Q":
    value = int(inputStr)
    if value < smallest:
        smallest = value
    inputStr = input("Enter a value or 'Q' to quit: ")
print("The smallest value is: ", smallest)
