from abc import ABC


class Dish(ABC):
    def __init__(self, name: str, weight: int, ingredients: list, price: float):
        self.name = name
        self.weight = weight
        self.ingredients = ingredients
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("You must add name for the dish!")
        self.__name = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if not value:
            raise ValueError('You must add weight for the dish!')
        if not isinstance(value, int):
            raise ValueError('Weight must be integer!')
        self.__weight = value

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, value):
        if not value:
            raise ValueError('You must add list of ingredients for the dish!')
        self.__ingredients = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value == '':
            raise ValueError('You must add price for the dish!')
        if not value.isfloat():
            raise ValueError('You must add float number as price(for example : 1,99)!')
        self.__price = value
