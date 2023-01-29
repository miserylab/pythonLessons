# str_1 = "hello"
# str_2 = 'WORLD'
# print(str_1)
# print(dir(str_1))
# print(str_1.upper())
# print(str_1.title())
#
# print(str_2)
# print(str_2.lower())
# -----------------------
# name = 'Ivan'
# a = 'Hello {}'
# result = a.format(name)
# print(result)
# -----------------------
first_name = 'Ivan'
last_name = 'Ivanov'
a = '{} {}'
result = a.format(first_name, last_name)
print("Меня зовут : " + result)

result = f'{first_name} {last_name}'
print(result)