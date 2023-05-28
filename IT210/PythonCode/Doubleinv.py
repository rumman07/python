##
#This program computes the time to double an investment.
#

#Create constants variable.
RATE = 5.0
INITIAL_BALANCE = 10000.0
TARGET = 2 * INITIAL_BALANCE

#initialize variable
balance = INITIAL_BALANCE
year = 0

#count the years required to double the investment

while balance < TARGET:
    year = year + 1
    interest = balance * RATE / 100
    balance = balance + interest
#print the result
print("The investment doubled after", year, "years")

    
