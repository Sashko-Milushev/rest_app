from dish_structure.dish import Dish


class Bread(Dish):
    def __init__(self, name: str, weight: int, ingredients: list, price: float):
        super().__init__(name, weight, ingredients, price)
