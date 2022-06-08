#Gary j Jenks
#WordGuess
#6/8/2022
#programs goal is to make a basic guessing game 
#one user inputs a word for a secret word variable 
#second user guesses and checks secret word

userSecret = input("Set your secret word: ")
guess = ""
turn = 3
isPlay = True

while guess != userSecret or turn == 0:
    guess = input("You have " + str(turn) + " turns left Enter Guess: ")
    turn -= 1
    if turn == 0 :
        break
   
if turn == 0:
    print("Out of guesses please play again")
else:
    print("Nice guess!!")