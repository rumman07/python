names = ["Rumman","Saad","Salman","Shaheed","Ronty"]

def main():

    k = display(names)
    print(k)
    seperator()

def display(names):
    name = " "
    for element in names:
        name = name + element
    return name

def seperator():
    for i in range(len(names)):
        if i > 0:
            print(">>>>", end = " ")
        print(names[i], end = " ")
    
main()



        
