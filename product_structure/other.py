from product_structure.product import Product


class Other(Product):
    def __init__(self, name: str):
        super().__init__(name)

    def __repr__(self):
        return f'{self.name} from type: {__class__.__name__}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('You must add name for the product!')
        self.__name = value
