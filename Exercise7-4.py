prompt = "\nPlease choose your Pizza's ingredient:"
prompt += "\nEnter 'quit' to exit choose"

active = True
ingredients = []
while active:
    ingredient = input(prompt)

    if ingredient != 'quit':
        ingredients.append(ingredient)
        print(prompt)

    elif ingredient == 'quit':
        active = False

print(f"\nYou's choose for the Pizza is :")
for ingredient in ingredients:
    print(ingredient.title())