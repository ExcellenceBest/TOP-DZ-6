"""Задание 1 Реализуйте класс автомобиль, конструктор класса, метод для вывода по умолчанию, методы валидации
для атрибутов, реализуйте доступы к отдельным атрибутам через методы объекта(геттере и сеттеры)"""
class Auto:
    def __init__(self, mark: str, model: str, year_of_production: int, color: str, price: float, equipment: dict, acceleration: float):
        self.mark = mark
        self.model = model
        self.year_of_production = year_of_production
        self.color = color
        self.price = price
        self.equipment = equipment
        self.acceleration = acceleration

    def validation_mark(mark) -> str:
        if len(mark) == 0:





    def __str__(self):
        return (f'Марка Авто: {self.mark} \n'
                f'Модель Авто: {self.model}\n'
                f'Год выпуска: {self.year_of_production}\n'
                f'Цвет кузова Авто: {self.color}\n'
                f'Цена Авто: {self.price}\n'
                f'Комплектация Авто: {self.equipment}\n'
                f'Разгон до 100 км\ч,сек: {self.acceleration}')


car = Auto( '','ix35', 2013, 'grey',1300000,
           {'Коробка передач': "automat", 'Электропакет': "full", 'Тип': "petrol",
            'Объем двигателя': 2.0, 'Производитель': 'Korea'}, 7.8)
print(car)
