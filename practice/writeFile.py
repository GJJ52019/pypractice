#writing to files practice
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! using "w" will delete everything in existing file!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#however using "w" allows for the creation of new files 
# example text_file = open("text1.txt", "w") creates a new file
# can be used to write htmls as well

text_file = open("text.txt","a") # use "a" to append o to the end of the file use "w" to override the whole file 

text_file.write("\nAlien vs Predator is the next file there was never a fourth one")# will apend twice watch out for messing up files

text_file.close