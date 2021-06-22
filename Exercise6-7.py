peoples = {
    'x': {
        'first_name': 'X',
        'last_name': 'xx',
        'age': '12',
        'location': 'GuangZhou',
    },
        'y': {
        'first_name': 'Y',
        'last_name': 'yy',
        'age': '14',
        'location': 'ShenZhen',
    },
        'z': {
        'first_name': 'Z',
        'last_name': 'zz',
        'age': '16',
        'location': 'GuangZhou',
    },
        'm': {
        'first_name': 'M',
        'last_name': 'mm',
        'age': '12',
        'location': 'HeNan',
    },
        'n': {
        'first_name': 'N',
        'last_name': 'nn',
        'age': '20',
        'location': 'Beijing',
    },
}

for people, people_info in peoples.items():
    full_name = f"{people_info['first_name']} {people_info['last_name']}"
    age = people_info['age']
    location = people_info['location']
    print(f"\t{people}'s fullName is {full_name}")
    print(f"\t{people}'s age is {age}")
    print(f"\t{people}'s location is {location}")