def add_num(*num):
    sum = 0
    fornt = []
    for i in num:
        i = str(i)
        for k in i:
            fornt.append(k)#เก็บไว้แสดง output
            k = int(k)
            sum+=k
    out = ' + '.join(fornt)+' = '+str(sum)
    return out
print(add_num(12,13)) #output: 1 + 2 + 1 + 3 = 7
print(add_num(21,23,34,56)) #output: 2 + 1 + 2 + 3 + 4 + 5 + 6 = 23
print(add_num(49,52,54,56,58,60)) #output: 4 + 9 + 5 + 2 + 5 + 4 + 5 + 6 + 5 + 8 + 6 + 0 = 59
