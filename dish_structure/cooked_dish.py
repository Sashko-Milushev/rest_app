from dish_structure.dish import Dish


class CookedDish(Dish):
    def __init__(self, name: str, weight: int, ingredients: list, price: float):
        super().__init__(name, weight, ingredients, price)

