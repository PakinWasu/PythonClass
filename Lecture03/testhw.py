


for muti in range(27,31):
    print('-------------')
    print('     %d      '%muti)
    print('-------------')
    for num in range(1,13,1):
        sum = muti * num
        print(f"{muti:>2} x {num:>2} = {sum:>3}")
    print()