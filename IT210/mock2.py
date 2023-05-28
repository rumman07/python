# compute the mean of 10 input values and count the number of thosew
#values which are greater than the mean, and the number which are
#less than the mean.  The input values will be placed in a list.

myList = []
for i in range(10):
    val = float(input("Please enter a value: "))
    myList = myList + [val]

#Compute the mean
sum = 0
for i in range(len(myList)):
            sum = sum + myList[i]
mean = sum / len(myList)


#Now count the number of values greater than the mean and the number
#of values less than the mean.
greater = 0
less = 0
equal = 0
for i in range(len(myList)):
        if myList[i] > mean:
               greater = greater + 1
        elif myList[i] < mean:
               less = less + 1
        else:
           equal = equal + 1


print("Mean",mean)
print("greater", greater)
print("Less", less)
print("Equal", equal)
               
