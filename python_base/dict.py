# список
family_1 = ['Alex', 'Ivan', 'Peter', 'Sidor', 'Fedor', 'Alex']
print(family_1)

# множества
family_2 = {'Alex', 'Ivan', 'Peter', 'Sidor', 'Fedor', 'Alex'}
print(family_2)

# словарь (ключ: значние)
family_tree = {"Папа": 'Alex', "Мама": 'Ivan', "Сын": 'Peter', "Дочь": 'Sidor'}
print(family_tree["Сын"])
for k, v in family_tree.items():
    print(k + ' - ' + v)