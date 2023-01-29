# age =20
# name = 'Ale'
#
# if age == 25 or name == 'Alex':
#     print('Мне 25 лет и меня зовут Алекс')
# # elif age > 25:
# #     print('Мне больше 25 лет')
# else:
#     print("Мне меньше 25 лет")

#------------------------------

# name = 'Alex'
#
# if 'a' in name == 'Alex':
#     print('Меня зовут Алекс')
# else:
#     print('Меня не зовут Алекс')

pin = 1234
print("Введите пожалуйста Ваш пин-код")
user_pin = int(input())
if pin==user_pin:
    print("Какую сумму вы хотите снять")
else:
    print("Ошибка. Введите корректный пин-код, у Вас осталось две попытки")
    user_pin = int(input())
    if pin == user_pin:
        print("Какую сумму вы хотите снять")
    else:
        print("Ошибка. Введите корректный пин-код, у Вас осталась одна попытка")
        user_pin = int(input())
        if pin == user_pin:
            print("Какую сумму вы хотите снять")
        else:
            print("Ошибка. Ваша карта заблокирована. Обратитесь в банк")