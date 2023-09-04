import math
print('1-100')
columns = int(input('How many columns? :'))
row = math.ceil(100/columns)
n=1
for r in range(row):
    for c in range(columns):
        print(n,end="\t")
        n = n+1
        if n > 100:
            print('')
    print('')