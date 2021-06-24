# 创建一个用于存储外星人的空列表
aliens = []

#创建30个绿色的外星人
for alien in range(30):
    new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = '10'

#显示前5个外星人：
for alien in aliens[:5]:
    print(alien)
print('.............')

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = '10'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['point'] = '20'

#显示前5个外星人：
for alien in aliens[:5]:
    print(alien)
print('.............')
