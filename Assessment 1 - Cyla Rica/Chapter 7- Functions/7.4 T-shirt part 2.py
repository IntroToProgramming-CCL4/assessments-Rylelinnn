def make_shirt(size="large", message="I love Python"):
    """Prints a sentence summarizing the size and message of the shirt."""
    print(f"Making a shirt of size {size.upper()} with the message: '{message}'.")

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt(size="medium")

# Make a custom-sized shirt with a different message
make_shirt(size="small", message="Python Rocks!")