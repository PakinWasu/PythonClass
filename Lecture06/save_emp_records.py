def main():
    numEmps = int(input('How many employee records ' + \
                        'do you want to create?'))
    empFile = open ('employees.txt', 'w')

    for count in range(1, numEmps + 1):
        print('Enter data for employee #', count, sep='')
        name = input('Name: ')
        idNum = input('ID number: ')
        dept = input('Department: ')

        empFile.write(name + '\n')
        empFile.write(idNum + '\n')
        empFile.write(dept + '\n')


        print()

    empFile.close()
    print('Employee records written to employees.txt.')

main()