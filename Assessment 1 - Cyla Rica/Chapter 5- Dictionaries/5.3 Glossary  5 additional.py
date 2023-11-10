# Create a glossary dictionary with programming words and their meanings
glossary = {
    'variable': 'A container for storing data values.',
    'function': 'A reusable block of code that performs a specific task.',
    'list': 'A collection of items in a particular order.',
    'loop': 'A programming structure that repeats a sequence of instructions.',
    'dictionary': 'A collection of key-value pairs.'
}

# Add five more terms to the glossary
glossary['module'] = 'A file containing Python code that can be imported and used in another program.'
glossary['class'] = 'A blueprint for creating objects with shared attributes and behaviors.'
glossary['method'] = 'A function that is associated with an object and can be called on that object.'
glossary['inheritance'] = 'A way to create a new class using properties and methods of an existing class.'
glossary['exception'] = 'An event that occurs during the execution of a program and disrupts its normal flow.'

# Print each word and its meaning with a loop
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")