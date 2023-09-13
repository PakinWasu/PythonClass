import pickle

def main():
    endOfFile = False
    
    inputFile = open('info.dat','rb')

    while not endOfFile:
        try:
            person = pickle.load(inputFile)

            displayData(person)
        except EOFError:

            endOfFile = True

    inputFile.close()

def displayData(person):
    print('Name: ', person['name']) 
    print('age: ', person['age'] ) 
    print('weight: ', person['weight'] ) 

main()
    