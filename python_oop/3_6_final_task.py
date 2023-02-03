__author__ = 'miserylab'

class Car:
    '''Создаём машину'''

    def __init__(self, model, year, engine_volume, price, mileage):
        '''Инициализируем атрибуты машины'''
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.price = price
        self.mileage = mileage
        self.num_wheels = 4
        self.type_of_car = 'Машина'

    def description(self):
        '''Получаем описание машины'''
        description = 'модель: ' + self.model + ', \nгод выпуска: ' + str(self.year) + ', \nобъем двигателя: ' + \
                      str(self.engine_volume) + ', \nцена: ' + str(self.price) + ', \nпробег: ' + str(self.mileage)+ \
                      ', \nколичество колёс ' + str(self.num_wheels) + '\n '
        print(self.type_of_car + ': \n' + description)

class Truck(Car):
    '''Создаём грузовик'''

    def __init__(self, model, year, engine_volume, price, mileage):
        '''Инициализируем атрибуты грузовика'''
        super().__init__(model, year, engine_volume, price, mileage)
        self.num_wheels = 8
        self.type_of_car = 'Грузовик'


car = Car("Tesla Car", 2020, 600, 750000, 12000)
car.description()

truck = Truck("Tesla Truck", 2022, 500, 500000, 8000)
truck.description()