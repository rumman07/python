##
#This program prints a table showing the gorwth of an investment.
#

#Define constant variable
RATE = 5.0
INITIAL_BALANCE = 10000.0

#Obtain the number of years for the computation
numYears = int(input("Enter number of years: "))

#Print the table of balance for each year
balance = INITIAL_BALANCE
for year in range (1, numYears + 1):
    interest = balance * RATE / 100
    balance = balance + interest
    print("%4d %10.2f" % (year, balance))
    
    
    
