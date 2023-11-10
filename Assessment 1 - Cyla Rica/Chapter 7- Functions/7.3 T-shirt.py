def make_shirt(size, message):
    """Prints a sentence summarizing the size and message of the shirt."""
    print(f"Making a shirt of size {size.upper()} with the message: '{message}'.")

# Call the function using positional arguments
make_shirt("medium", "Keep Calm and Code On")

# Call the function using keyword arguments
make_shirt(size="large", message="I Love Python")