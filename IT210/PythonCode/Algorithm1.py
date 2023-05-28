#Sum amd average algorithm
total = 0
count = 0
inputStr = input("Enter value: ")
while inputStr != "Q":
    value = float(inputStr)
    total = total + value
    count = count + 1
    inputStr = input("Enter value or Q to quit: ")
print("The total is: ", total)    
if count > 0:
    average = total / count
    print("The average is:%.2f " % average)
else:
    print("No data")
    
