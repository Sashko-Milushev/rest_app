from product_structure.other import Other


class Cleaning(Other):
    def __init__(self, name: str, quantity: str, purpose: str, price: float):
        super().__init__(name)
        self.purpose = purpose
        self.quantity = quantity
        self.price = price

    @property
    def purpose(self):
        return self.__purpose

    @purpose.setter
    def purpose(self, value):
        if value == '':
            raise ValueError('You must add purpose for the cleaning agent!')
        self.__purpose = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value == '':
            raise ValueError('You must add quantity for the cleaning agent!')
        self.__quantity = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value == '':
            raise ValueError('You must add price for the cleaning agent!')
        if not value.isfloat():
            raise ValueError('You must add float number as price(for example : 1,99)!')
        self.__price = value
