import math
print('1-100')
col = int(input('How many col:'))
row = math.ceil(100/col)
n = 1
for i in range(row):
    for k in range(col):
        print(n,end=' ')
        if (k+row) %col == col:
            print()
        n = n+1
    print() 
#จำไม่ได้แต่ให้เขียนตาม flowchart ผลลัพประมาณนี้แต่เรียงสวยกว่านี้