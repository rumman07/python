from random import shuffle 

#This function takes a list shuffles it and then returns the list
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

#This function takes the user's guess
def user_guess():
    guess = ""

    while guess not in ["0","1","2"]:
        guess = input("Pick a number from 0, 1, and 2:")
    return int(guess)

#This function takes the shuffled list and the user guess and checks whether the user have guess correctly
def check_guess(mylist, guess):
    if mylist[guess] == "O":
        print("Correct Guess!")
        print(mylist)
    else:
        print("Wrong Guess!")
        print(mylist)

#This is the control-plane of the program!

mylist = [" ", "O", " "]

shuffled_list = shuffle_list(mylist)

guess = user_guess()

check_guess(shuffled_list,guess)

