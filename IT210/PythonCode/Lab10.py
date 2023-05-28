#Rumman Ahmed Lab#10
'''The following program will read in the Cartesian coordinates for
two points, and then compute and output the slope of the line
passing through these two points, as well as the distance between
the two points.  You are to modify this code so that it will
catch and handle at least TWO DIFFERENT TYPES of exceptions.
You do NOT have to give the user a second chance at anything,
simply print an appropriate message and terminate the program normally.'''

import math 
x1Str = input("Enter the x-coordinate of the first point") 
y1Str = input("Enter the y-coordinate of the first point")
x2Str = input("Enter the x-coordinate of the second point")
y2Str = input("Enter the y-coordinate of the second point")

try: 
 x1 = int(x1Str)
 y1 = int(y1Str)    #int() can raise a value error exception
 x2 = int(x2Str)
 y2 = int(y2Str)

 slope = (y2 - y1)/(x2 - x1)
  #Distance can be negative.
 #distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
 distance = (x2 - x1) + (y2 - y1)
 if distance < 0:
     raise ArithmeticError("Distance can't be negative")

 print("The slope is ", slope)
 print("The distance between the points is ", distance)

except ValueError:
    print("Error: Invalid input value")
except RuntimeError as error:
    print("Error:", str(error))
    
    

          
    
