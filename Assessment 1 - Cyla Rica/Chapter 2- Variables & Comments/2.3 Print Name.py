# Define a variable for a person's name with whitespace characters
person_name = "\t\t John Smith \n"

# Print the name with leading and trailing whitespace
print(f'Name with whitespace: "{person_name}"')

# Print the name after stripping leading whitespace
print(f'Name after lstrip: "{person_name.lstrip()}"')

# Print the name after stripping trailing whitespace
print(f'Name after rstrip: "{person_name.rstrip()}"')

# Print the name after stripping both leading and trailing whitespace
print(f'Name after strip: "{person_name.strip()}"')