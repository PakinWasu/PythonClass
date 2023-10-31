def sumTwosmallestNums(num):
    num = sorted(num)
    #print(num)
    number = 0
    r = 0
    for i in num:
        if i >= 0 :
            number = number + i
            r = r+1
            if r == 2:
                return(number)
print(sumTwosmallestNums([19,5,42,2,77]))

print(sumTwosmallestNums([10,343445353,3453445,3453545353453]))
print(sumTwosmallestNums([2,9,6,-1]))
print(sumTwosmallestNums([879,953,694,-847,342,221,-91,-723,791,-587]))
print(sumTwosmallestNums([3683,2902,3951,-475,1617,-2385]))