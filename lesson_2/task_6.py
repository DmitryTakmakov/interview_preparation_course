"""
Проверить на практике возможности полиморфизма. Необходимо разделить дочерний
класс ItemDiscountReport на два класса. Инициализировать классы необязательно.
Внутри каждого поместить функцию get_info, которая в первом классе будет
отвечать за вывод названия товара, а вторая — его цены. Далее реализовать
выполнение каждой из функции тремя способами.
"""


class ItemDiscount:
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


class ItemDiscountReportPrice(ItemDiscount):
    def __init__(self, parent_object: ItemDiscount):
        super().__init__(parent_object.name, parent_object.price)

    @property
    def get_info(self) -> int:
        return self.price


class ItemDiscountReportName(ItemDiscount):
    def __init__(self, parent_object: ItemDiscount):
        super().__init__(parent_object.name, parent_object.price)

    @property
    def get_info(self) -> str:
        return self.name


def main():
    item = ItemDiscount('Test item', 10000)
    report_classes = (ItemDiscountReportPrice, ItemDiscountReportName,)
    for cls in range(len(report_classes)):
        rep = report_classes[cls](item)
        print(f'Regular call: {rep.get_info}')
        print(f'getattr call: {getattr(rep, "get_info")}')


if __name__ == '__main__':
    main()
