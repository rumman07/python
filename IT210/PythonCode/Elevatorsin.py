##
#This program simulates an elevator panel that skips the 13th floor.
#

#Obtain the floor number from the user as an integer.

floorNumber = int(input("Please enter the floor number: "))

#Adjust floor if necessary

if floorNumber>13:
    actualFloor = floorNumber - 1
else:
    actualFloor = floorNUmber

#Print the result
print("The elevator will travel to the actual floor: ", actualFloor)


    
