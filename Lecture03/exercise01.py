#Print the table headings
print('-------------')
print('KPH\t MPH')
print('-------------')

#Print the Number 1 through 10
#and their squares.
for kph in range(60,131,10):
    mph = kph*0.6214
    print(kph,'\t','%.1f'%mph)