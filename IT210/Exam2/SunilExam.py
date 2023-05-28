def main():
    #opening file for reading
    file = open("Ex2.txt")
    listOfStrings = []

    #saving each line in the file 
    for line in file:
        listOfStrings.append(line.strip())
    file.close() #clising th efile

    #master list to store each line as a list
    listOfLists = []

    #converting each lie string into a list and appending to the maste rlist
    for item in listOfStrings:
        listOfLists.append(convertToList(item))

    #printing the master list to dmonstrate that it was created properly
    print("Printing the master list to dmonstrate that it was created properly:\n")
    printList(listOfLists)
    print("")

    #updating the end of semester results
    print("\n\nEnter end of semester updates:\n\n" )
    
    for item in listOfLists:
        #displaying current details
        print("Name: ",item[0]," ",item[1])
        print("Tech ID: ",item[2])
        print("No of credits Earned: ",item[3])
        print("No of Quality points earned: ",item[4])
        print("Enter values to add to the record: ")

        #askign user for what values to add
        cc = int(input("Enter No of Credits Completed: "))
        qp = int(input("Enter No of Quality points earned: "))
        
        #adding the vaues and saving it into the list
        item[3]= int(item[3])+cc
        item[4]=int(item[4])+qp
        
        print("")

    #printing the master list with updated values to dmonstrate that it was created properly
    print("\n\nPrinting the master list with updated values to dmonstrate that it was created properly: \n")
    printList(listOfLists)

    
    #opening file to save data into
    file = open("out.txt",'w')
    for item in listOfLists:
        #converting each item of the master list into a string
        strValue = convertToString(item)
        strValue+="\n" #adding new line at the end of evrey record
        #writing the record into the file
        file.write(strValue)

    #closing the file
    file.close()

    print("\n\nFinifhed saving results to out.txt")

#this function converts the input string into a list
def convertToList(line):
    #removing all leading and trailing white space characters as they are not desired
    retVal = line.strip().split()
    return retVal

#this function converts the input list into a string
def convertToString(item):
    retVal = ""
    #iterating through the list to merge to the string
    for val in item:
        #converting each elemnt into a string as they may be an int
        #as converted while adding the current semester results
        retVal += str(val);
        #adding a space at the end of each item in the list
        retVal+=" "
    #returning the result
    return retVal

#this function will pritn the result
def printList(l):
    for item in l:
        print(item)
main()
