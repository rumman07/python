#Rumman Ahmed Exam2
'''Python program reads data for several students from a text file and create a master list
   to store the data.The program iterate through the master list and asks the user for end-of-the-semester updates.
   These values are then added and updated to the master list.'''

#This is the main function
def main():
    inFile = open("Ex2.txt", "r")
    stringList = []

    #Spliting each word in the line and storing it 
    for line in inFile:
        stringList.append(line.strip())
    inFile.close()

    #master list to store each line as a list
    masterList = []


    for item in stringList:
        masterList.append(convertToList(item))

    #printing the masterList
    print("Printing the master list:\n")
    printList(masterList)
    print()

    #Updating results
    print("\n Enter end of semester results:\n" )
    
    for item in masterList:
        print("FirstName: ",item[0])
        print("LastName: ", item[1])
        print("Tech ID: ",item[2])
        print("Credits Completed: ",item[3])
        print("Quality Points Earned: ",item[4])
        print("Enter values to add to the record: ")

        #Prompt user to enter credits completed and quality points earned at the end of the semester
        creditsCompleted = int(input("Enter No of Credits Completed: "))
        qualityPointsEarned = int(input("Enter No of Quality points earned: "))
        
        #Updating Credits completed and Quality points earned
        item[3]= int(item[3])+ creditsCompleted
        item[4]=int(item[4])+ qualityPointsEarned
        print()

    #Printing the masterList 
    print("\n Print the master list: \n")
    printList(masterList)

    
    #Writing the output to a file
    outputFile = open("outt.txt",'w')
    for item in masterList:
        val = convertToString(item)
        val = val + "\n" #adding new line at the end of evrey record
        outputFile.write(val)

    
    outputFile.close()

    print("Please check the output file to verify the results")

#This function converts the input string into a list
def convertToList(line):
    listVal = line.strip().split()
    return listVal

#This function converts the input list into a string
def convertToString(item):
    stringVal = ""
    for value in item:
        stringVal = stringVal + str(value);
        stringVal = stringVal + " "
    return stringVal

#Displaying the output
def printList(l):
    for item in l:
        print(item)
main()
