from product_structure.other import Other


class Decoration(Other):
    def __init__(self, name, quantity, price):
        super().__init__(name)
        self.price = price
        self.quantity = quantity
