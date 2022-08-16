from product_structure.product import Product


class Drinks(Product):
    def __init__(self, name: str, quantity: str, expiration_date: str, price: float):
        super().__init__(name)
        self.price = price
        self.quantity = quantity
        self.expiration_date = expiration_date

    def __repr__(self):
        return f'{self.quantity} {self.name} with expiration_date: {self.expiration_date}'

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value == '':
            raise ValueError('You must add quantity for the drink product!')
        self.__quantity = value

    @property
    def expiration_date(self):
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        if value == '':
            raise ValueError('You must add expiration date for the drink product!')
        self.__expiration_date = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value == '':
            raise ValueError('You must add price for the drick!')
        if not value.isfloat():
            raise ValueError('You must add float number as price(for example : 1,99)!')
        self.__price = value
