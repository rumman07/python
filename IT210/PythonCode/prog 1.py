#Rumman Ahmed Program 1
speed = int(input("Enter the speed here: "))

if (speed > 70):
    fine = 50 + 15 * (speed - 55)
    print("Fine for the speeding ticket $", fine)
elif(speed > 60 and speed <= 70):
    fine = 25 + 5 * (speed - 55) 
    print("Fine for the speeding ticket $", fine)
elif(speed > 55 and speed <= 60):
    print("Caution crossing speed limit")
elif(speed == 55 ):
    print("At the speed limit")
else:
    print("Normal driving!")

    
reply = input("Please 'C' to continue or 'Q' to quit: ")


while reply == "C":
    speed = int(input("Enter the speed here: "))

if (speed > 70):
    fine = 50 + 15 * (speed - 55)
    print("Fine for the speeding ticket $", fine)
elif(speed > 60 and speed <= 70):
    fine = 25 + 5 * (speed - 55) 
    print("Fine for the speeding ticket $", fine)
elif(speed > 55 and speed <= 60):
    print("Caution crossing speed limit")
elif(speed == 55 ):
    fine
    print("At the speed limit")
else:
    if reply == "Q":
        print("Good Bye!")
        
    
    






   

