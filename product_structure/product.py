from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('You must add name of the product!')
        self.__name = value
