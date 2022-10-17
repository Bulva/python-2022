
slovnik = {
    'NAME': None,
    'RESIDENCE': None,
    'AGE': None,
    'TYPE': [{
        'VEHICLE_REGISTRATION_PLATE': None,
        'CATEGORY': None,
    }]
}
# print(slovnik)

name, residence, age, vehicle, category = input('NAME: '), input('RESIDENCE: '), input(
    'AGE: '), input('VEHICLE_REGISTRATION_PLATE: '), input('CATEGORY: ')
print(name, residence, age, vehicle, category)
