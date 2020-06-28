# 1. Write a Python function to find the Max of three numbers.
def find_max(num1, num2, num3):
    # return max(num1, num2, num3)
    if (num1 > num2):
        if(num1 > num3):
            return num1
        return num3
    else:
        if num2 > num3:
            return num2
        return num3


print(find_max(100, 20, 30))
