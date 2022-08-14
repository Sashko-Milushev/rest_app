from product_structure.other import Other


class SugarPacks(Other):
    def __init__(self, name, quantity, type_of_sugar, price):
        super().__init__(name)
        self.quantity = quantity
        self.type_of_sugar = type_of_sugar
