##
#This program simulates an elevator panel thar skips the 13th floor.
#checking for input errors.
#

#Obtain the floor number from the user as an integer.
floor = int(input("Floor: "))

#Make sure the user input is valid.
if floor == 13:
    print("Error: There is no thirteenth floor.")
elif floor <= 0 or floor > 20:
    print("Error: The floor must be between 1 and 20.")
else:
    #now we know the input is valid
    actualFloor = floor
    
