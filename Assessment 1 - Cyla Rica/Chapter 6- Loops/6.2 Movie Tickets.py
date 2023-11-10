# Start a loop to ask users for their age
while True:
    # Ask the user for their age
    age_str = input("Enter your age (or 'quit' to exit): ")

    # Check if the user wants to quit
    if age_str.lower() == 'quit':
        break

    # Convert age to an integer
    age = int(age_str)

    # Determine the cost of the movie ticket based on age
    if age < 3:
        ticket_cost = 0
    elif 3 <= age <= 12:
        ticket_cost = 10
    else:
        ticket_cost = 15

    # Print the cost of the movie ticket
    print(f"The cost of your movie ticket is ${ticket_cost}\n")
