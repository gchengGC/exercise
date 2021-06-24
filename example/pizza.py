#存储所点的披萨信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
#概述所点的披萨
print(f"You ordered a {pizza['crust']} - crust pizza")
for topping in pizza['toppings']:
    print("\t" + topping)