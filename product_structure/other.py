from product_structure.product import Product


class Other(Product):
    def __init__(self, name):
        super().__init__(name)

    def __repr__(self):
        return f'{self.name} from type: {__class__.__name__}'