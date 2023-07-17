hours_worked = int(input('Enter the number of hours worked: '))
pay_rate = int(input('Enter the hourly pay rate: '))

if hours_worked > 40:
    print('The gross pay is $'+format((40*pay_rate)+((hours_worked - 40)*(pay_rate*1.5)),',.2f')+".")
else :
    print('The gross pay is $'+format((hours_worked*pay_rate),',.2f')+".")
