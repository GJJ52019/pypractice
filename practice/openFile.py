#opening files with write and read
#use .readable to tell if the file is readable must use "r" in the open()
#use .read to access all the information in a file 
#use .readline to get individual lines use in consecutives to print lines in order
#use .readlines()[index] to specify lines 

#r for read
text_file = open("text.txt","r") #opens the file in read only

for line in text_file.readlines():
    print(line)


text_file.close() # always close files