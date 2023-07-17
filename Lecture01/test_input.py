#Get the user's first name.
# first_name = input('Enter your first name: ')

# #Get the user's last name.
# last_name = input('Enter your last name: ')

# #print a greeting to the user
# print('Hello',first_name,last_name)

# Get the user's name, age, and income
name = input('What your name? ')
age = int(input('What is your age? '))
income = float(input('What is your income? '))

#Display the data
print('Here is the data you entered: ')
print('Name:',name)
print('Age:',age)
print('Income:', format(income, ',.2f'))