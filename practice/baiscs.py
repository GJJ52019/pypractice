#exponents
print(2**3)
# function to return inputed power
def exponential(base, power):
    results = 1
    for index in range(power):
        results = results * base
    return results

print(exponential(3,4))