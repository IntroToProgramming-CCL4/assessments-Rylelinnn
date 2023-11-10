# Initialize an empty list to store pizza toppings
pizza_toppings = []

# Start a loop to prompt the user for pizza toppings
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ").lower()

    # Check if the user wants to quit
    if topping == 'quit':
        break

    # Add the topping to the list
    pizza_toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

# Print the final list of pizza toppings
print("\nYour pizza toppings:")
for topping in pizza_toppings:
    print(topping.title())