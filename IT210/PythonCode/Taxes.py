##
#This program computes income taxes, using a simplified tax schedule
#

#Initialize constant variable for the tax rates and rate limit
RATE1 = 0.10
RATE2 = 0.25
RATE1_SINGLE_LIMIT = 32000.0
RATE1_MARRIED_LIMIT = 64000.0

# Read income and maritial status.
income = int(input("Please enter your income: "))
maritialStatus = input("Please enter 'S' for Single and 'M' for Married Maritial Status: ")


#Compute taxes due
tax1 = 0.0
tax2 = 0.0

if maritialStatus == "S":
    if income <= RATE1_SINGLE_LIMIT :
       tax1 = RATE1 * income
    else:
        tax1 = RATE1 * RATE1_SINGLE_LIMIT
        tax2 = RATE2 * (income - RATE1_SINGLE_LIMIT)
        
        
else:
    if income <= RATE1_MARRIED_LIMIT:
        tax1 = RATE1 * income
    else:
        tax1 = RATE1 * RATE1_MARRIED_LIMIT
        tax2 = RATE2 *(income - RATE1_MARRIED_LIMIT)

totalTax = tax1 + tax2
print("Total tax amount:$%.4f" %(totalTax))
