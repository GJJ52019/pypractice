#place basics here

#string reverse using [::-1]
string = "0123456789"

print(string[::-1])




#math functions can be found at https://www.programiz.com/python-programming/modules/math
#use bin() to get binary representation convert back with int(binary, base) ie int(0b101, 2) = 5 
#complex() for situations with imaginary numbers


#exponents
print(2**3)
# function to return inputed power
def exponential(base, power):
    results = 1
    for index in range(power):
        results = results * base
    return results

print(exponential(3,4))