from product_structure.food import Food


class Vinegar(Food):
    def __init__(self, name: str, quantity: str, expiration_date: str, price: float):
        super().__init__(name, quantity, expiration_date, price)

