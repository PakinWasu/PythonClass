def numberSplit (num):
    int(num)
    if num%2 != 0 and num > -1:
        num1 = int(num/2)
        return [num1+1,num1]
    elif num%2 != 0 and num < 0 :
        num1 = int(num/2)
        return [num1-1,num1]
    else:
        num1 = int(num/2)
        return [num1,num1]


print(numberSplit(4))
print(numberSplit(10))
print(numberSplit(11))
print(numberSplit(-9))

#เฉลย
# def numberSplit (num):
#     return [num//2,num//2+num%2]

# print(numberSplit(4))
# print(numberSplit(10))
# print(numberSplit(11))
# print(numberSplit(-9))