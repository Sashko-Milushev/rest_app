from product_structure.other import Other


class SugarPacks(Other):
    def __init__(self, name: str, quantity: str, type_of_sugar: str, price: float):
        super().__init__(name)
        self.quantity = quantity
        self.type_of_sugar = type_of_sugar
        self.price = price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value == '':
            raise ValueError('You must add quantity for the sugar packs!')
        self.__quantity = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value == '':
            raise ValueError('You must add price for the sugar pack!')
        if not value.isfloat():
            raise ValueError('You must add float number as price(for example : 1,99)!')
        self.__price = value

    @property
    def type_of_sugar(self):
        return self.__type_of_sugar

    @type_of_sugar.setter
    def type_of_sugar(self, value):
        if value == '':
            raise ValueError('You must add type of sugar(for example : white/brown)!')
        self.__type_of_sugar = value
