import pickle

def main():
    again = 'y'

    outputFile = open('info.dat','wb')

    while again.lower()== 'y':
        saveData(outputFile)

        again = input('Enter more data? (y/n): ')

    outputFile.close


def saveData(file):
    person = {}

    person['name'] = input('Name: ')
    person['age'] = int(input('Age: '))
    person['weight'] = float(input('Weight: '))

    pickle.dump(person, file)

main()