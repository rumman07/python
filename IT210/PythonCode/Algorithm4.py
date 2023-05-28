#Maximum
largest = int(input("Enter a value: "))
inputStr = input("Enter value: ")
while inputStr != "Q":
              value  = int(inputStr)
              if value > largest:
                  largest = value
              inputStr = input("Enter value or 'Q' to quit: ")
print("The largest value is: ", largest)

