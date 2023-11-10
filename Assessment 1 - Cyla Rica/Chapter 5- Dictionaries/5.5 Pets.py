# Create a list of dictionaries representing different pets
pets = [
    {'kind': 'dog', 'owner': 'Andy'},
    {'kind': 'cat', 'owner': 'Jace'},
    {'kind': 'parrot', 'owner': 'Charles'},
    {'kind': 'fish', 'owner': 'Cyla'},
    {'kind': 'rabbit', 'owner': 'Tisha'}
]

# Loop through the list and print information about each pet
for pet in pets:
    print(f"Kind of animal: {pet['kind'].title()}")
    print(f"Owner's name: {pet['owner'].title()}")
    print()