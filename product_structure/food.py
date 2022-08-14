from product_structure.product import Product


class Food(Product):
    def __init__(self, name: str, quantity: str, expiration_date: str):
        super().__init__(name)
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
            raise ValueError('You must add quantity of the food product!')
        self.__quantity = value

    @property
    def expiration_date(self):
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        if value == '':
            raise ValueError('You must add expiration date for the food product!')
        self.__expiration_date = value
