#Lab3 Rumman Ahmed
#Read user input hours worked and hourly rate
hours = float (input("ENTER THE HOURS WORKED AS INTEGER"))
rate = float (input("Enter the hourly pay rate as an integer"))
if hours > 40:
    gross = 40 * rate + (hours - 40) * rate * 1.5
    print ("Overtime")

else:
    gross = hours * rate
    print("no overtime:")
print("The gross wage is", gross)

numberOfDependents = int(input("Please enter number of dependents: "))
netwage = gross - (50 * numberOfDependents)
print(netwage)
                         
                         
