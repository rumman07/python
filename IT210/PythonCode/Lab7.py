#Rumman Ahmed Lab#7
##
#Write function for the following.
#average of two numbers return the result.
#one number raised to the power of a second one return the result.
#Absolute value number return result.
#find the larger of two numbers and return the result.
#num = 2
#num1 = 3



def averageTwoNumber(num, num1):
    avg = (num + num1) / 2
    return avg

def powerSecondNumber(num):
    power =(num)**(num + 1)
    return power

def absoluteValNumber(num):
    absolute = int(num)
    return absolute

def largerOfTwoNumber(num, num1):
    if num > num1:
        return num
    else:
        return num1

##
#Testing
#print(averageTwoNumber(num, num1))
#print(powerSecondNumber(num))
#print(absoluteValNumber(num))
#print(largerOfTwoNumber(num, num1))
#
      
