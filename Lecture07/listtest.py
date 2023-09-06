def findBigestNum(nums):
    bigest = nums[0]
    for i in nums:
        if i > bigest:
            bigest = i
    return(bigest)

listnum = [4,5,6,17,3,2,9]

print(findBigestNum(listnum))
print(max(listnum))
print(min(listnum))