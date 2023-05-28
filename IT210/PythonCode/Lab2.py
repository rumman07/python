import math 
#Rumman Ahmed Lab2
#This program is an extension to Lab1 

#Declaring Variable
diameter = float(input("Enter an integer diameter of a Cylinder: "))
height = float(input("Enter an Integer Height for the Cylinder: "))

radius= diameter/2
surface_area=0
volume=0

#Computing surface area of the cylinder
surface_area = (2*math.pi*radius)*(radius + height)
volume = math.pi * (radius**2) * height

#surface_area = '%.2f' % (surface_area)
#volume = '%.2f' % (volume)

#Output
print("The surface area of the cylinder is :", '%.2f' % surface_area)
print("The Volume of the cylinder is :", '%.2f' % volume)
