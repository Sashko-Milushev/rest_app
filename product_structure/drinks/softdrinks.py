from product_structure.product import Product


class SoftDrink(Product):
    def __init__(self, name: str, quantity: str, price: float):
        super().__init__(name)
        self.quantity = quantity
        self.price = price
