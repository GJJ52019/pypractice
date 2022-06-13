#example of managing list and 2d list with loops 

#list within a list that creates a grid 4 rows 3 columns
#do not forget the comma's (,) between each index
numbers = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]

]

#acessing list within list 
# prints 3rd row 2nd column which is 8
print(numbers[2][1])

#nested loop to acess the 2d list
#creates variables row and col
#starts by going to row[0] col[0]
#iterates through each index and prints its
#moves to next row till all are complete
for row in numbers:
    for col in row:
        print(col)

#more list examples
letterSoup = ['a','a','e','d','d','c','x','s']
print(letterSoup)
letterSoup.sort() #sorts string list in alphabetical order
print(letterSoup)
letterSoup.reverse() # reverses list
print(letterSoup)

newLetterSoup = letterSoup[::-1] #when ussing the [::-1] it creates a new list and does not update the old one
print(newLetterSoup)
print(letterSoup)


addToSent = " "

sentence = addToSent.join(["hey", "my","name","isn't","Jack","its","John"])
print(sentence)