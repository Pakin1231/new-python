heros = ['Ironman', 'Thor', 'Hulk', 'Superman', 'Spiderman']
h2 = ['Dr.Strange', 'Cpt.America', 'Black Panther', 'Ant Man']

heros.insert(0, h2[0])
print(heros.index('Thor'))
heros.insert(heros.index('Thor'), h2[1])
print(heros)