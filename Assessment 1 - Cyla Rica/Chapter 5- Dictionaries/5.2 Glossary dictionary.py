# Create a glossary dictionary with programming words and their meanings
glossary = {
    'variable': 'A container for storing data values.',
    'function': 'A reusable block of code that performs a specific task.',
    'list': 'A collection of items in a particular order.',
    'loop': 'A programming structure that repeats a sequence of instructions.',
    'dictionary': 'A collection of key-value pairs.'
}

# Print each word and its meaning with a newline between each pair
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")