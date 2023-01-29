class Person():
    '''Создаём человека'''

    def __init__(self, name, age, height, weight):
        '''Инициализируем атрибуты человека'''
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def description_person(self):
        '''Получаем описание человека'''
        description = self.name + ', ему ' + str(self.age) + ', его рост ' + str(self.height) + ', его вес ' + str(self.weight)
        print('Нового человека зовут : ' + description)

    def get_weight(self):
        '''Получаем вес человека'''
        print("Вес нашего человека : " + str(self.weight))

    def update_weight(self, kg):
        '''Изменяем вес человека'''
        self.weight = kg



man = Person('Alex', 30, 180, 100)
man.description_person()
# man.weight = 110
man.update_weight(115)
man.get_weight()