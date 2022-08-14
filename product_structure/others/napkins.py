from product_structure.other import Other


class Napkins(Other):
    def __init__(self, name, quantity, type_of_napkins, price):
        super().__init__(name)
        self.quantity = quantity
        self.type_of_napkins = type_of_napkins
        self.price = price
