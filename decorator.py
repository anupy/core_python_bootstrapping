def function_outer(number):
    def inner_facto(number):
        if number <= 1: return 1
        print(number)
        rnum = inner_facto(number - 1)
        print(rnum)
        num = number * rnum
        return num
    return inner_facto(number)

@function_outer(5)
def checking_decorator():
    pass

print(checking_decorator())
