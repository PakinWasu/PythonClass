#This program calculates the sum of a series
#of number entered by the user
max = 5 #The maximum number
#Initialize an accumulator
total = 0.0
print('This program calculates the sum of')
print(max,'numbers you will enter.')

for count in range(max):
    number = int(input('Enter a number: '))
    total = total + number

print('The total is',total)
