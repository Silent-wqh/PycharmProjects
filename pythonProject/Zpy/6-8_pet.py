huanhuan = {'type': 'dog', 'owner': 'Amy'}
pipi = {'type': 'dog', 'owner': 'Bob'}
miaomiao = {'type': 'cat', 'owner': 'Cindy'}

pets = [huanhuan, pipi, miaomiao]

for pet in pets:
    for key, value in pet.items():
        print(f'{key}  {value}')