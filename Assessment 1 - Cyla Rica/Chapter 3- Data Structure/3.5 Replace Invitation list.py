# Define a list of people to invite to dinner
invitees = ["Albert Einstein", "Leonardo da Vinci", "Marie Curie"]

# Print the name of the guest who can't make it
guest_cant_make_it = "Albert Einstein"
print(f"{guest_cant_make_it} can't make it to the dinner.\n")

# Replace the guest who can't make it with a new person
new_invitee = "Isaac Newton"
invitees.remove(guest_cant_make_it)
invitees.append(new_invitee)

# Print a second set of invitation messages
for invitee in invitees:
    print(f"Dear {invitee},\nYou are cordially invited to a dinner at my place. Please join us for an evening of great conversation and good food!\n Sincerely, Cyla \n")
