def fun (i):
    print("Initial value of i in the function", i)
    i = i + 5
    print("The new value odf i in the function", i)

def fun2(list):
    print("The initial content of the list in the function", list)
    list[0] = 9999999
    print("The new content of the list", list)

def main():
    i = 42
    fun(i)
    print("In main the value of the variable", i)

    list = [2,3,4,-45,123,9]
    fun2(list)
    print("In main the contain of the list", list)

main()
