import re


def many_arg(a, b, c, d, e, f, g, h):
    print(c,a,b,b,a,g,e)


def many_nested_if(num1, sign, num2):
    if num1 > 0:
        if num1 < 6:
            if num2 > 0:
                if num2 < 6:
                    if num1:
                        if num1 == 1 and sign == '+' and num2 == 1:
                            print("1+1 = 2")
                        if num1 == 1 and sign == '+' and num2 == 2:
                            print("1+2 = 3")
                        if num1 == 2 and sign == '+' and num2 == 2:
                            print("2+1 = 3")
                        if num1 == 2 and sign == '+' and num2 == 2:
                            print("2+2 = 4")
                        if num1 == 3 and sign == '+' and num2 == 1:
                            print("3+1 = 4")
                        if num1 == 1 and sign == '+' and num2 == 3:
                            print("1+3 = 4")
                        if num1 == 4 and sign == '+' and num2 == 1:
                            print("4+1 = 5")
                        if num1 == 3 and sign == '+' and num2 == 2:
                            print("3+2 = 5")
                        if num1 == 2 and sign == '+' and num2 == 3:
                            print("2+3 = 5")
                        if num1 == 1 and sign == '+' and num2 == 4:
                            print("1+4 = 5")


def many_nested_return(num1, num2):
    if num1 > 0:
        if num1 > 1:
            if num1 < 3:
                if num2 > 0:
                    if num2 > 1:
                        if num2 < 3:
                            return 2 + 2
                        return 2 + 2
                    return 2 + 1
                return 2
            return 3
        return 1
    return 0