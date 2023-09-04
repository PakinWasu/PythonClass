month = [31,28,31,30,31,30,31,31,30,31,30,31]
def what_fristday_month(day,M_month):
    n=0
    sumday =0
    for i in month:
        if n == M_month-1:
            break
        n = n+1
        sumday = sumday+i
    sumday = sumday+day
    frist_day_month = (sumday-2)%7
    return (frist_day_month)
M_month = int(input('What month of 2023: '))
frist_day = what_fristday_month(1,M_month)
#print(frist_day)
print('='*32)
print('M    T    W    T    F    S    S')
print('='*32)
for i in range(frist_day):
    print(' ',end='    ')
for day in range(1,month[M_month-1]+1):
    print(f'{day:<2}',end='   ')
    if (frist_day+day)%7 == 0:
        print()
print()
print('='*32)