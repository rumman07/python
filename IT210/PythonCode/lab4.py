#Rumman Ahmed Lab4. 
choice= input("Press 'C' for temp in Celciue or 'F' for temp in Fahrenheit: ")

if(choice!="C" and choice!="F"):
    print("ERROR IN INPUT")
else:
    temp= float(input("Please enter temperature: "))

    for i in range(1,11):
        V=i*5
        if(choice == "C"):
            WC=35.74+0.6215*temp-3.75*V**0.16+0.4275*temp*V**0.16
        else:
            WC=13.12+0.6215*temp-11.37*V**0.16+0.3965*temp*V**0.16
        print("{0:.3f}".format(WC),end=' ')
