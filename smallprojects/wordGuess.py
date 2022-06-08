#Gary j Jenks
#WordGuess
#6/8/2022
#programs goal is to make a basic guessing game 
#one user inputs a word for a secret word variable 
#second user guesses and checks secret word

userSecret = input("Set your secret word: ") # user inputed secret
guess = "" #second users guess

isPlay = "y" 


while isPlay == "y":
    turn = 3 # turn counter
    guessCount = 0
    while guess != userSecret or turn == 0:
        guess = input("You have " + str(turn) + " turns left enter an guess: ")
        turn -= 1
        if turn <= 0:
            break
   
    if turn == 0 and guess != userSecret:
        print("\nOut of guesses would you like to play again\n")
        isPlay = input('Press "Y" for yes or "N" for no: ').lower()
    else:
        print("Nice guess!! You win!!")