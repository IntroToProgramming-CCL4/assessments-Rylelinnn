# Define a list of people to invite to dinner
invitees = ["Albert Einstein", "Leonardo da Vinci", "Marie Curie" , "Isaac Newton", "Lisa Monoban"]

# Print a message indicating that only two people can be invited
print("Unfortunately, the dinner table won't arrive in time, and we can only invite two people for dinner.\n")

# Use pop() to remove guests and print apology messages
while len(invitees) > 2:
    removed_guest = invitees.pop()
    print(f"Sorry, {removed_guest}, but we can't invite you to dinner this time.")

# Print invitation messages to the two remaining guests
for invitee in invitees:
    print(f"Dear {invitee},\nYou are still invited to dinner. Please join us for an evening of great conversation and good food! \nSincerely, Cyla \n")

# Use del to remove the last two names from the list
del invitees[:]

# Print the list to ensure it's empty
print("Remaining guests list:", invitees)