import math
##
#Rumman Ahmed Lab#6
#This program compares the values (expressed in cost per square inch)
#of three sizes of pizzas.
#call our 3 variable for the values
#valSm, valMed, + valLg
#com[are these and find the minimum.
#if valSm<valMed and valSm < valLg
#print("small pizza is the best")
#

diamSm = float(input("Please enter diameter for a small pizza: "))
costSm = float(input("Please enter the cost of a small pizza: : "))
diamMed = float(input("Please enter diameter for a medium pizza: "))
costMed = float(input("Please enter the cost of a medium pizza: "))
diamLg = float(input("Please enter diameter for a large pizza: "))
costLg = float(input("Please enter the cost of a large pizza: "))

def Pizza_Value_Calc(diam, cost):
    areaOfPie = math.pi*(diam /  2)**2
    value = cost / areaOfPie
    return value

valSm = Pizza_Value_Calc(diamSm, costSm)
valMed = Pizza_Value_Calc(diamMed, costMed)
valLg = Pizza_Value_Calc(diamLg, costLg)

if valSm < valMed and valSm < valLg:
    print("The small pizza is the best deal")
elif valMed < valSm and valMed < valLg:
    print("The medium pizza is the best deal")
elif valLg < valMed and valLg < valSm:
    print("The large pizza is the best deal")
else:
    print("The xLarge pizza is the best deal")
    

    
                     
