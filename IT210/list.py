'''This program demonstrates three different ways of getting data from a
user and placing it in a Python list.  The first loop assumes that the input
values are in the range 0 throuhg 100 (such as exam percentages) and uses a
sentinel of a negative value to terminate the loop.  The second loop first
asks the user how many values there are and uses a counter to control the loop.
The third loop asks the user each time if there is another value and uses the
response to control the loop.  In each case, the list contests are printed out
both element-by-element and as an entire list.  If you run this with the same
basic input data values, you should get the same out put three times.'''

'''This is the one that uses a sentinel.  We'll use a negative value for the
sentinel.  We can't just assign to a list without first creating it.
We'll create it as being initially empty and then use list concatenation (+)
to add new items'''

myList1 = []
i = 0 #index value
val = int(input("Enter number from 0 through 100, enter a negative to quit"))
while val > 0:
    myList1 = myList1 + [val]
    i = i + 1
    val = int(input("Enter number from 0 through 100, enter a negative to quit"))

print(myList1)

for i in range(0, len(myList1)):
        print(myList1[i])

'''This is the loop that asks the user how many values there are and uses
that value to control the loop.  Again we'll create an initially empty
list and concatenate each value to it in turn'''

myList2 = []
howMany = int(input("How many data values are there?"))
for i in range (howMany):
    val = int(input("Please enter a value:"))
    myList2 = myList2 + [val]

print(myList2)

for i in range(len(myList2)):
    print(myList2[i])


'''This is the loop that asks the user each time if there is a data
value to be entered'''

myList3 = []
ans = input("Is there more data to enter?(Y or N)")
while ans =="Y":
            val = int(input("Please enter a value: "))
            myList3 = myList3 + [val]
            ans = input("Is there more data to enter?(Y or N)")

print(myList3)

for i in range(len(myList3)):
            print(myList3[i])

            

    
            
        
               
    
    
