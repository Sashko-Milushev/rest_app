from product_structure.drinks import Drinks
from product_structure.food import Food
from product_structure.other import Other

chicken_fillet = Food('Chicken fillet', '225g', '19/08/2022')
lemonade = Drinks('Homemade lemonade', '330ml', '18/08/2022')
napkins = Other('Luxury napkins')

print(chicken_fillet)
print(lemonade)
print(napkins)