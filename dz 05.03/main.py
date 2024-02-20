"""Задание 1. Реализуйте класс Автомобиль"""

class Auto:
    def __init__(self, mark: str, model: str, year_of_production: int, color: str, price: float, equipment: dict, acceleration: float):
        self.mark = mark
        self.model = model
        self.year_of_production = year_of_production
        self.color = color
        self.price = price
        self.equipment = equipment
        self.acceleration = acceleration


    def __str__(self):
        return (f'Марка Авто: {self.mark} \n'
                f'Модель Авто: {self.model}\n'
                f'Год выпуска: {self.year_of_production}\n'
                f'Цвет кузова Авто: {self.color}\n'
                f'Цена Авто: {self.price}\n'
                f'Комплектация Авто: {self.equipment}\n'
                f'Разгон до 100 км\ч,сек: {self.acceleration}')


car = Auto("Hyundai", 'ix35', 2013, 'grey',1300000,
           {'Коробка передач': "automat", 'Электропакет': "full", 'Тип': "petrol",
            'Объем двигателя': 2.0, 'Производитель': 'Korea'}, 7.8)
print(car)



"""Задание 2. Реализуйте класс Стадион"""

class Stadium:
    import datetime
    def __init__(self, title: str, open_date: datetime, country: str, city: str, capacity: int, architect: str):
        self.title = title
        self.open_date = open_date
        self.country = country
        self.city = city
        self.capacity = capacity
        self.architect = architect

    def __str__(self):
        return (f'Название Стадиона: {self.title}\n'
                f'Дата открытия стадиона: {self.open_date}\n'
                f'Страна: {self.country}\n'
                f'Город: {self.city}\n'
                f'Вместимость стадиона: {self.capacity}\n'
                f'Архитекторы: {self.architect}')



stadium1 = Stadium('Альянц Арена','2005/5/30', 'Germany',
                   'Munich', 71137, 'бюро Herzog & de Meuron Architekten')


print(stadium1)



