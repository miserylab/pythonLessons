personal = ['Alex', 'Ivan', 'Peter', 'Sidor']
#             0        1       2        3
result = personal[0] + ' ' + personal[2]
print(result + ' - лучшая пара')

number = [1 , 15, 23, 4, 5]
#         0   1   2   3
num_1 = number[1]
print(num_1)
result_num = number[1] + number[3]
print(result_num)


print(len(personal))

print(personal[-1]) # обращение к последнему элементу из списка
print(personal[0:3])
print(personal[1:])

personal.append('Fedor')
print(personal)

pn = []
pn.append(personal)
pn.append(number)
print(pn)