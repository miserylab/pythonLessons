a =int(input('Введите первое значение: '))
b =int(input('Введите первое значение: '))


try:
    result = int(a / b)
except ZeroDivisionError:
    result = 0
    print("На 0 делить нельзя")

print("Результат: " + str(result))

result_2 = a + b
print(result_2)

# ZeroDivisionError