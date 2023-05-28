#Rumman Ahmed Lab9
'''The following program reads from one text file and copies it exactly, line
per line to an ouput text file.'''

#Open two files one in read mode and one in write mode.
inFile = open("LabInputFile.txt", "r")
outFile = open("LabOutputFile.txt", "w")

#Write a header to the output file, just so you can see the difference
print("This is the output file", file = outFile)

#Write to the screen just to see that you still can, even when you are using
#files for some of the output.
print("We're ready to start reading the file")

#The following "for: loop will iterate through the input file one line at a
#time. Each line that is read in is convert into a list which contains the
#5 individual items of data. The list is written out to "LabOutputFile.txt"
#The end = ' ' prevents an extra newline at the end of each line. Note that this
#is two apostrophes, not a quote mark.
for line in inFile:
    values = [line]
    print(values, file = outFile, end = ' ')
#Close both files.
inFile.close()
outFile.close()

    
