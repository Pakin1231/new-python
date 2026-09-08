phonebook = {'Anirah': '777-1111', 'Mickey': '777-2222', 'Donald': '777-3333', 'Pluto': '777-4444'}

heroesdict = {}
heroesdict['Hulk'] = '888-1111'
heroesdict['Ironman'] = '888-2222'
print(heroesdict.get('Hulk', 'Key not found'))  # Output: 888-1111
print(heroesdict.get('Halk', 'Key not found'))  # Output: Key not found

for key, value in phonebook.items():
    print("{key}: {value}")

print(phonebook.keys())  # Output: dict_keys(['Anirah', 'Mickey', 'Donald', 'Pluto'])
print(phonebook.values())  # Output: dict_values(['777-1111', '777-2222', '777-3333', '777-4444'])
print(phonebook.pop('Mickey', 'Element not found'))  # Output: 777-2222
print(phonebook.pop('Mick', 'Element not found'))  # Output: Element not found
print(phonebook)  # Output: {'Anirah': '777-1111', 'Donald': '777-3333', 'Pluto': '777-4444'}
print(phonebook.popitem())  # Output: ('Pluto', '777-4444')
print(phonebook)  # Output: {'Anirah': '777-1111', 'Donald': '777-3333'}
phonebook.clear()
print('After clear')
print(phonebook)  # Output: {}