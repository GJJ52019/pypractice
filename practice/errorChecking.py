#try and except practice

# written as is leads to input error
# 
# num = int(input("Please enter a number: "))
# print(num)

#use of try/except to handle invalid inputs
try:
    num = int(input("Please enter a number: "))
    print(num)
except:
    print("please only use integers")