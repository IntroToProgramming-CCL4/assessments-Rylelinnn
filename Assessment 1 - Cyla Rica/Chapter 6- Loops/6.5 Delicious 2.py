# Make a list called sandwich_orders and fill it with the names of various sandwiches
sandwich_orders = ['ham and cheese', 'turkey', 'BLT', 'tuna', 'chicken', 'pastrami', 'pastrami', 'pastrami']

# Make an empty list called finished_sandwiches
finished_sandwiches = []

# Print a message saying the deli has run out of pastrami
print("Sorry, the deli has run out of pastrami.\n")

# Remove all occurrences of 'pastrami' from sandwich_orders using a while loop
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through the list of sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

# Print a message listing each sandwich that was made
print("\nFinished Sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.title())
