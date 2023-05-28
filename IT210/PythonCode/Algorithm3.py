#Prompt utill a match is found
valid = False
while not valid:
    value = int(input("Please enter a positive vlaue < 100: "))
    if value > 0 and value < 100:
                valid = True
    else:
                print("The value is not valid")
