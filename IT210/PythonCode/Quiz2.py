def main():
    windSpeed = 0
    temp = 0

    for i in range (1, 11):
        V=i*5
    WC = 35.74+0.6215*temp-3.75*V**0.16+0.4275*temp*V**0.16

    #temperature
    for temp in range (-45, 40, 5):
        print (2*" ",temp, end=" ")
    print("\n"," "*2,"-"*105)    

    #Wind Speed
    for windSpeed in range (0, 60, 5):
        print(windSpeed)
main()
