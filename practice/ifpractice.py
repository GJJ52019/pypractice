#basic ifs

#bool if
is_male = True
is_tall = False

#starts with if, then the question, the the condtion  
#else to handle other options
# when using or it triggers the if when one of the questions is true
# use and  to force both questions to have to be true
#use not to force the opposite bool
if is_male and is_tall:
    print("you are tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but are tall")
else:
    print("you are not male or not tall")