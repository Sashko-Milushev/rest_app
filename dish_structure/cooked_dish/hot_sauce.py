from dish_structure.cooked_dish import CookedDish


class HotSauce(CookedDish):
    def __init__(self, name: str, weight: int, ingredients: list, price: float):
        super().__init__(name, weight, ingredients, price)
