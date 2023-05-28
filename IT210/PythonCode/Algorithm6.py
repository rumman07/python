#Computing adjacent value
value = int(input("Enter a value: "))
inputStr = input("Enter a value: ")
while inputStr != "Q":
    previous = value
    value = int(inputStr)
    if value == previous:
        print("Duplicate Entry")
    inputStr = input("Enter a value or 'Q' to quit: ")
    
