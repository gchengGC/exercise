places = ['jiu zhai gou', 'huang shan', 'hua shan', 'xi zang', 'si chuan']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

if List:
    print('List is not Null')

Dictionary = {'x':'1','y':'2'}
x = Dictionary['x']
Dictionary['z'] = 3
del Dictionary['x']
m = Dictionary.get('m', 'No m value assigned.')

for key, value in Dictionary.items():
for k, v in Dictionary.items():
for name in Dictionary.keys():
for name in Dictionary:

if 'n' not in Dictionary.keys():
    print('Dictionary don\'t have n')

for name in sorted(Dictionary.keys()):

for value in Dictionary.values():

for value in set(Dictionary.values()):