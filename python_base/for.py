students = ['Alex', 'Ivan', 'Peter', 'Sidor', 'Igor', 'Svetlana']
#             0        1       2        3       4          5
for f in students:
    if f == 'Peter':
        var = 'Инженер ' + f
        print(var)


for f in students[:4]:
    print(f)


for f in students:
    print(len(f))