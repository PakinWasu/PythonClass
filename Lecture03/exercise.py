columns= int(input('How many columns? '))
for num in range(1,101):
    print(f'{num:>3}',end=" ")
    if(num%columns) == 0:
        print()