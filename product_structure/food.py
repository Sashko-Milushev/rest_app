from product_structure.product import Product


class Food(Product):
    def __init__(self, name, quantity, expiration_date):
        super().__init__(name)
        self.quantity = quantity
        self.expiration_date = expiration_date

    def __repr__(self):
        return f'{self.quantity} {self.name} with expiration_date: {self.expiration_date}'