from product_structure.product import Product


class Drinks(Product):
    def __init__(self, name, quantity, expiration_date):
        super().__init__(name)
        self.quantity = quantity
        self.expiration_date = expiration_date
