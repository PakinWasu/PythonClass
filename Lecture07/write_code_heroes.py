heroes = ['Ironman', 'Thor','Hulk','Spiderman']
pro = True
def main():
    print('''Please select option -
    1. Display Heroes
    2. Add Heroes
    3. Insert Heroes
    4. Remove Heroes
    5. Display Sorted Heroes(Ascending/Descending)''')
    select_options = int(input('Select operations form 1,2,3,4,5 : '))
    if select_options == 1:
        display()
    elif select_options == 2:
        add_heroes()
    elif select_options == 3:
        insert_heroes()
    elif select_options == 4:
        remove_heroes()
    elif select_options == 5:
        sorte_name()
    else:
        print('Select 1,2,3,4,5')
    print()
def display():
    print('\n')
    print(heroes)
def add_heroes():
    name = input('Name Heroes : ')
    heroes.append(name)
def insert_heroes ():
    name = input('Name Heroes : ')
    ind = str(len(heroes)-1)
    index = int(input('Enter index want insert pls enter 0-'+ind+' : '))
    while index > len(heroes)-1 or index < 0:
        index = int(input('Enter index want insert pls enter 0-'+ind+' : '))
    heroes.insert(index,name)
def remove_heroes():
    name = input('Name Heroes remove : ')
    while not(name in heroes):
        print('Dont have this name')
        name = input('Name Heroes remove : ')
    heroes.remove(name)
def sorte_name():
    print('''Please select option -
    1. Ascending
    2. Descending    ''')
    slc = int(input('Select operations form 1,2: '))
    if slc == 1:
        heroes.sort(key=len)
    elif slc == 2:
        heroes.sort(key=len)
        heroes.reverse()

while pro:
    main()
