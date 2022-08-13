from abc import ABC


class Product(ABC):
    def __init__(self, name, product_type):
        self.name = name
        self.product_type = product_type

    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        if value in 'Food Other Drink':
            self._product_type = value
        else:
            raise Exception('Invalid product type!')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value != '':
            self._name = value
        else:
            raise Exception('Name can not be empty string!')