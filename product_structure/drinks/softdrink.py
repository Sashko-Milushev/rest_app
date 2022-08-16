from product_structure.drinks import Drinks


class SoftDrink(Drinks):
    def __init__(self, name: str, quantity: str, expiration_date: str, price: float):
        super().__init__(name, quantity, expiration_date, price)