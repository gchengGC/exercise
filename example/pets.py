pets = ['dogs', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')