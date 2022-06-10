#for loop practice
#works very simialr to javascript for loops
#for in loops creates an variable  that iterates through arrays

# loops one time for each letter 
# letter becomes a defined variable

for letter in "Xenomorph":
    print(letter)

#prints each iteration of the array 
movies = ["alien", "aliens", "alien 3", "Jurassic Park"]

for movie in movies:
    print(movie)

# example of range() and looping through numbers
#range(starting value, finish value not included)
for index in range(2,20):
    print(index)

#use range to print out movies array.
for movie in range(len(movies)):
    print(movies[movie])

for index in range(15):
    if index == 0: 
        print ("first place")