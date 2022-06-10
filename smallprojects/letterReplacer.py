#Gary Jenks
#6/10/2022
#program is to replace specified letters during specified instance
#example: replace all vowels with certain character
#log
#first attempt on if statement used == instead of in causing failed attempt

def replacer(passedWord):
    replace = ""
    for let in passedWord:
        if let in "AEIOUaeiou": # if letter is in specified target string replaces with x
            replace = replace + "x"
        else:
            replace = replace + let
    return(replace)



print(replacer(input("Please enter a word or phrase: ")))