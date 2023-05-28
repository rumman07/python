perc = float(input("What percentage did you earn?"))

if perc >= 90:
    print ("Great job")
    print ("You got an A")
else:
    if perc >= 80:
        print ("Good work")
        print ("You got a B")
    else:
        if perc >= 70:
            print ("Meh")
            print ("You got a C")
        else:
            if perc >= 60:
                print ("Try harder")
                print ("You got a D")
            else:
                print ("AARHH")
                print ("You got an F")


if perc >= 90:
    print ("A")
elif perc >= 80:
    print ("B")
elif perc >= 70:
    print ("C")
elif perc >= 60:
    print ("D")
else:
    print ("F")
                
        
