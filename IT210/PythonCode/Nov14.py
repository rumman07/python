def fun(i):
    print("Initial value of i in the function", 1)
    i = i + 5
    print ("new value of i in the function", i)
    
def fun2(list):
    print("Initial list contents in the function", list)
    list[0] = 9999999
    print("new value of list in the function", list)

def main():
    #the main program
    i = 42
    fun(1)
    print("in main the value of the variable is", i)
    #print("in main the value of the parameter is", 1)

    list = [3, 88, -65, 19, 27, 9]
    fun2(list)
    print("in main the list content is" list)

main()    
    
    
