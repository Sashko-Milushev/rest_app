from dish_structure.cold_dish import ColdDish


class Salad(ColdDish):
    def __init__(self, name: str, weight: int, ingredients: list, price: float):
        super().__init__(name, weight, ingredients, price)

