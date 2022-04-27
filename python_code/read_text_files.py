#Old sytle of opening and reading a file with way you need to manually close the file 
file1 = open('text.txt')
print(file1.read())
print(type(file1))
file1.close()

#New way of opening and reading a file with this style you don't need to manually close a file 
with open('myfile.txt') as file2:
    contents = file2.read()
print(contents)

#Creating and writing on a file
with open('text2.txt', mode='w') as f: 
    f.write("This is the first line")
    
#Appending some text on an existing file
with open('text.txt', mode='a') as line:
    line.write(" These text were generated by hipster.")

#Overwriting a file
z = open('text2.txt', 'w')
z.write("Overwriting")
z.close()

#Appending to the same file
k = open('text2.txt', 'a')
k.write("\n")
k.write("Appending text")
k.close()