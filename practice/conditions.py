#function max_num retuns largest passed number

def max_num(num1, num2, num3):
    high_num = 0

    if num1 > num2 and num1 > num3:
        high_num = num1
    elif num2 > num1 and num2 > num3:
        high_num = num2
    elif num3 > num1 and num3 > num2:
        high_num = num3

    return print(high_num)


max_num(476,50,300)