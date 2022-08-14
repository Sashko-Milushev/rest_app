from product_structure.other import Other


class Cleaning(Other):
    def __init__(self, name, quantity, purpose, price):
        super().__init__(name)
        self.purpose = purpose
        self.quantity = quantity
        self.price = price
