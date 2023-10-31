def highestDigit(num):
    numhigh = 0 
    num = str(num)
    #print(type(num))

    for number in num:
        number = int(number)
        #print(number)
        if numhigh < number :
            numhigh = number
    return numhigh
print(highestDigit(379))


print(highestDigit(2))

print(highestDigit(377401))

