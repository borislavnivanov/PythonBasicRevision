positions = input()

animals_list: list = positions.split(', ')

wolf_position = animals_list.index('wolf') + 1

if wolf_position == len(animals_list):
    print('Please go away and stop eating my sheep')
else:
    closest_animal = len(animals_list) - wolf_position
    print(f'Oi! Sheep number {closest_animal}! You are about to be eaten by a wolf!')
