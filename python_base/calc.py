a = int(input('Введите первое число: '))
m = input('Введите оператор(+, -, *, /): ')
b = int(input('Введите второе число: '))


if m == '+':
    result = int(a + b)
elif m == '-':
    result = int(a - b)
elif m == '*':
    result = int(a * b)
elif m == '/':
    try:
        result = int(a / b)
    except ZeroDivisionError:
        result = 0
        print("На 0 делить нельзя")
else:
    result = 0
    print("Введён некорректный оператор. Ожидается +, -, *, /")

print("Результат: " + str(result))

