bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}."

for i in bicycles:
    message = f"My first bicycle was a {i.title()}."
    print(message.title())

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(1, '2')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)
print(f"The last motorcycle I owned was a {poped_motorcycle.title()}.")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles.remove('suzuki')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

'''
numbers = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
last_number = []

for number in numbers:
    if number == 4 or number == 8:
        last_number.append(number)
        numbers.remove(number)
print(numbers)
print(last_number)
'''
