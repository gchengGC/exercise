cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print("Here is the original list:")
print(cars)

print("Here is the sorted list:")
print(sorted(cars))

print("Here is the reverse sorted list:")
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)

cars.reverse()
print(cars)