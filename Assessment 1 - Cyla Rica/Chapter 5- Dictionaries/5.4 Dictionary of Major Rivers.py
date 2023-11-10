# Create a dictionary of major rivers and the countries they run through
rivers = {
    'nile': 'Egypt',
    'amazon': 'Brazil',
    'yangtze': 'China'
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country}.")

# Print the names of each river
print("\nNames of each river:")
for river in rivers.keys():
    print(river.title())

# Print the names of each country
print("\nNames of each country:")
for country in rivers.values():
    print(country)