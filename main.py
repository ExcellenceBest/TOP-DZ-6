"""Задание 1
Реализуйте класс "Человек" , в полях класса:
ФИО, Дата рождения,контактный телефон, город, страна
домашний адрес.
Реализуйте конструктор по умолчанию и метод для вывода данных
"""
# Решение задачи №1
class Human:
    def __init__(self, name: str, data: str, phone: int, city: str, country: str, adress: str):
        self.name = name
        # FIXME: можно сделать типом date из модуля datetime
        self.data = data
        # FIXME: телефон не может быть целым числом
        self.phone = phone
        self.city = city
        self.country = country
        # FIXME: правильно address, можно сделать dict, т.к. нужно хранить отдельно город, улицу, дом, кв. и т.д.
        self.adress = adress

    def __str__(self):
        return (f'ФИО: {self.name} \n '
                f'Дата рождения: {self.data}\n'
                f'Телефон: {self.phone}\n'
                f'Город: {self.city}\n'
                f'Страна: {self.country}\n'
                f'Адрес: {self.adress}')

# FIXME: запрещаю использовать такие имена переменных, НИКАКОГО ТРАНСЛИТА!
chelovek = Human("Петр Яковлевич Бессмертных", '9 апреля 1984 г.', 352481, 'Ярославль', 'РОССИЯ', 'Ул. Свободы 1/2')
print(chelovek)

"""Задание 2
Реализуйте класс "Книга" в полях класса:
название книги, год выпуска, издателя, жанр, автора, цену
Реализуйте конструктор по умолчанию и метод для вывода данных
"""
# Решение задачи № 2
class book:
    def __init__(self, name: str, year: int, copyright: str, genre: str, autor: str, price: float):
        self.name = name
        self.year = year
        # FIXME: причем тут авторские права? Издатель - publisher
        self.copyright = copyright
        self.genre = genre
        self.autor = autor
        self.price = price

    def __str__(self):
        return (f'Название книги: {self.name}\n'
                f'Год выпуска: {self.year}\n'
                f'Издатель: {self.copyright}\n'
                f'Жанр: {self.genre} \n'
                f'Автор: {self.autor} \n'
                f'Цена книги: {self.price}')
book_1 = book('The Lord of Rings', 2002, 'ООО Печать', 'Fantasy', 'R.R.Tolkin', 999.99 )
print(book_1)

