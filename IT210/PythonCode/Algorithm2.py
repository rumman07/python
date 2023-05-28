#Counting matched Algorithm
negatives = 0
inputStr = input("Enter a value: ")
while inputStr != "Q":
    value = float(inputStr)
    if value < 0:
        negatives = negatives + 1
    inputStr = input("Please enter a value or 'Q' to quit: ")
print("There were", negatives, "negative values.")
