#Program gets inout and reads it back to the user

print("What is your favorite dinosaur?") 

myDino = input()

print(myDino + " is a really cool dinosaur!!") # prints name of dino inputed

print("The length of that dinosaur's name is:")
print(len(myDino)) # use len to find character count of a string

print("what is the year?")

currentYear = int(input()) #use int to convert strings to ints

noFish = 2050

yearsLeft = int(noFish) - int(currentYear)
print("There are only " + str(yearsLeft) + " until there might not be any fish left in the ocean.") # use str to convert int's to strings