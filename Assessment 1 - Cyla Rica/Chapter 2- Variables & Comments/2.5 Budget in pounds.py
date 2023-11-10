# Define the total budget in pounds
budget = 50

# Define the cost of each USB stick in pounds
usb_stick_price = 6

# Calculate the number of USB sticks she can buy
usb_sticks_to_buy = budget // usb_stick_price

# Calculate the remaining pounds
remaining_pounds = budget % usb_stick_price

# Print the results
print(f"The girl can buy {usb_sticks_to_buy} USB sticks.")
print(f"She will have £{remaining_pounds} left.")