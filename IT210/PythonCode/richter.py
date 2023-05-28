richter = float(input("Please enter richter: "))
if richter >= 8.0: #Handle the 'special case' first
    print("Most structures fall")
elif richter >=7.0:
    print("Many buildings destroyed")
elif richter >= 6.0:
    print ("Many buildings damaged, some collapse")
elif richter >= 4.5:
    print("Damage to poorly constructed buildings")
else: #so that the general can be handled last.
    print("No destruction of buildings")
    
