#This program will process a collection of 35 points of data. Each of
#these represents a student earned on exam. Find the highest and lowest
#percentages earned.

#Because these are percentages we can make the following initialization.
maximum = 0
minimum = 100
As,Bs,Cs,Ds,Fs = 0,0,0,0,0
avg = 0
total = 0

#Go through the loop 35 times
for count in range(35):
    value = float(input("PLease enter a percentage: "))
    if value > maximum:
        maximum = value
    if value < minimum:
        minimum = value
    #now let's work on the average
    total = total + value
    #now lets do grades
    if value >= 90:
        As = As + 1
    elif value >= 80:
        Bs = Bs +1
    elif value >= 70:
        Cs = Cs +1
    elif value >= 60:
        Ds = Ds +1
    else:
        Fs = Fs +1
        

print("The highest percentage is ", maximum)
print("The lowest percentage is ", minimum)
avg = total / (count + 1)
print("The class average is", avg)
print("There were", As, "A grades")
print("There were", Bs, "B grades")


#Add the following to the above program.
#have is compute and print the numbers of A's, B's, C's, D's, and F's
#      using the standard grading scale
#Have is compute and print the class average for the exam. 

#variable in program
#one variable for each kind of input.
#generally one variable for each different kind of output
#usually we will need some intermediate variable to get from the input to the output.
#placement of operatons with respect for a loop
#
    

