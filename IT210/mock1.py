'''Just testing my knowledge of python'''
def main():
    myList = [1,3,4,5,6,7]
    print(myList)
    print(multiply(myList, 100))
    print(userInput())
    
    
def multiply(list, factor):
    for i in range(len(list)):
        list[i] = list[i] * factor
    return list

def userInput():
    values = []
    print("Please enter integers or Q to quit")
    inputUser = input(" ")
    while inputUser.upper() != "Q":
          values.append(int(inputUser))
          inputUser = input(" ")
    return values      

main()

