from product_structure.other import Other


class Decoration(Other):
    def __init__(self, name, quantity: str, price: float):
        super().__init__(name)
        self.price = price
        self.quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value == '':
            raise ValueError('You must add quantity for the decoration!')
        self.__quantity = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value == '':
            raise ValueError('You must add price for the decoration!')
        if not value.isfloat():
            raise ValueError('You must add float number as price(for example : 1,99)!')
        self.__price = value
