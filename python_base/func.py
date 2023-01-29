# num_1 = 10
# num_2 = 20
# result = num_1 + num_2
# print(result)
#
#
# num_1 = 30
# num_2 = 40
# result = num_1 + num_2
# print(result)

def sum(num_1, num_2):
    result = num_1 + num_2
    print(result)

sum(10, 20)
sum(30, 40)
sum(num_2="Hello ", num_1="World")

name = input()
age = input()
def hi(name, age):
    result = name + ' ' + age
    return result

h = hi(name, age)
print(h)