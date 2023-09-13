phonebook = {'Anirach': '777-1111', 'Mickey': '777-2222',
            'Donald':'777-3333','Pluto':'777-4444'}

heroesdict = {}
heroesdict['Hulk'] = '888-1111'
heroesdict['Iron Man'] = '888-2222'
print(heroesdict.get('Halk', ' Key not found'))
print(heroesdict.get('Hulk', ' Key not found'))


for key, value in phonebook.items():
    print(key, value)

print(phonebook.keys())
print(phonebook.values())

print(phonebook.pop('Mick','Element not found'))
print(phonebook.pop('Mickey','Element not found'))
print(phonebook)
print(phonebook.popitem())
print(phonebook)
phonebook.clear()
print('After clear')
print(phonebook)