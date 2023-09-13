import pickle

def main():
    again = 'y'

    output_File = open('info.dat','wb')

    while again.lower()== 'y':
        saveData(output_File)

        again = input('Enter more data? (y/n): ')

    output_File.close


def saveData(file):
    
    person = {}
    try:
        person['name'] = input('Name: ')
        person['age'] = int(input('Age: '))
        person['weight'] = float(input('Weight: '))
        pickle.dump(person,file)
    except ValueError:
        print('ERROR: Age and Weight must be valid integers.')

    
main()