print('''Please select operation -
1. Add
2. Subtract
3. Multiply
4. Divide
''')
select_operations = int(input('Select operations form 1,2,3,4 : '))
first_number = int(input('Enter first number : '))
second_number = int(input('Enter second number : '))
if select_operations == 1:
    print(first_number,"+",second_number,"=",first_number+second_number)
elif select_operations == 2:
    print(first_number,"-",second_number,"=",first_number-second_number)
elif select_operations == 3:
    print(first_number,"*",second_number,"=",first_number*second_number)
else:
    print(first_number,"/",second_number,"=",first_number/second_number)
