#try and except practice

# written as is leads to input error
# 
# num = int(input("Please enter a number: "))
# print(num)

#use of try/except to handle invalid inputs
#best practice is to check for specific errors and print them.
try:
    num = int(input("Please enter a number: "))
    print(num)
except ZeroDivisionError as err: #specified exception catch, as allows the error to be printed as err
    print(err)
except ValueError: #input value error 
    print("please only use integers")