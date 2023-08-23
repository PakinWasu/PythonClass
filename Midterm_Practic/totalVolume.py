def totalVolume(*setnum):
    #print(len(setnum))
    number = 0
    for i in range(len(setnum)):
        numm = 1
        for num in setnum[i]:
            numm = numm*num
        number = number + numm
    return number

print(totalVolume([4,2,4],[3,3,3],[1,1,2],[2,1,1]))
print(totalVolume([2,2,2],[2,1,1]))
print(totalVolume([1,1,1]))