datalist = [[3,8,1],[0,4,7],[2,6,5]]
count = 0 
numlist = 0
data1 = []
resultlist = [[],[],[]]
#resultlist = [[0,0,0],[0,0,0],[0,0,0]] 
for i in range(3):
    for j in range(3):
        data1.append(datalist[i][j])
data1.sort()
for k in data1:
    if count > 2:
        numlist = numlist + 1
        count = 0
    resultlist[numlist].append(k)
    #resultlist[numlist][count] = k จำการใช้สลับกับarrayในc++
    count = count+1
print(resultlist)