##
#Rumman Ahmed Quiz2
#This program prints a table of Temperature Vs windchill for temperature
#in Fahrenheit.
#

for temp in range(40,-46,-5):
    print(temp, end='\t')
    for V in range(0,61,5):
        WC=13.12+0.6215*temp-11.37*V**0.16+0.3965*temp*V**0.16
        print("{0:.3f}".format(WC),end='    ')
    print('\n')
        
