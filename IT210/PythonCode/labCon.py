#here are the functions to do the two types of conversions.
def F_to_C(f):
    print("We're converting from Fahrenheit to Celsius")
    c = (f - 32) * (5 / 9)
    return c

def C_to_F(c):
    print("We're converting from Celsius to Fahrenheit")
    f = c * (9 / 5) + 32
    return f

def firstFunction():
    print("Welcome to the temperature conversion program. " )
    print("The program will convert either Fahrenheit to Celsius")
    print("or Celsius to Fahrenheit.")
    print("Please indicate which you would like to do.")
    ans = input("Enter FC for F to C or CF for C to F: ")
    return ans

def lastFunction():
    print("Thank you for your participation.")
    print("We look forward to serving all your future")
    print("temperature conversion needs.")
    
#now for the main program.
answer = firstFunction()

temp = int(input("Now please enter the temperature you want to convert:"))

if answer == "FC":
    cel = F_to_C(temp)
    print("YOur temperature in Celsius is", cel)
else:
    fahr = C_to_F(temp)
    print("Your temperature in Fahrenheit is", fahr)
    
lastFunction()     

#End of the Program. Developed by Rumman Ahmed.                  

    
