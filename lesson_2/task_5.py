"""
Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться
в качестве аргумента в дочерний класс. Выполнить перегрузку методов
конструктора дочернего класса (метод init, в который должна передаваться
переменная — скидка), и перегрузку метода str дочернего класса. В этом методе
должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно, не забудьте инициализировать дочерний и
родительский классы (вторая и третья строка после объявления дочернего класса).
"""


class Item:
    def __init__(self, name: str, price: int):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


class ItemDiscount(Item):
    def __init__(self, instance: Item, discount: int):
        self.discount = discount
        super().__init__(instance.name, instance.price)

    def __str__(self):
        return f'{self.price - int(self.price * (self.discount / 100))}'


def main():
    item = Item('Test item', 1000)
    discounted_item = ItemDiscount(item, 20)
    print(discounted_item)


if __name__ == '__main__':
    main()
