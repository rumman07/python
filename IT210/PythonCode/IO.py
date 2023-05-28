#Prompt for the input and output file names
inputFileName = input("Input file: ")
outputFileName = input("Output file: ")

#Open the input and output files.
inputFile = open(inputFileName, "r")
outputFile = open(outputFileName, "w")

for line in inputFile:
         #Make sure there is a space in the input file, otherwise skip the line
         if " " in line:
             #Split the record at the space.
             parts = line.split(" ")

             #Extract the data fields
             firstName = [parts[0]]
             lastName = [parts[1]]
             techId = [parts[2]]
             creditsTaken = [int(parts[3])]
             qualityPoints = [int(parts[4])]
        

             #Write the output
             #outputFile.write(firstName)
             #outputFile.write(lastName)
             #outputFile.write(techId)
             #outputFile.write(str("%-10s"%creditsTaken))
             #outputFile.write(str("%-10s"%qualityPoints))
             masterList = firstName + lastName + techId + creditsTaken + qualityPoints
             print(masterList)

#close file
inputFile.close()
outputFile.close()

             
