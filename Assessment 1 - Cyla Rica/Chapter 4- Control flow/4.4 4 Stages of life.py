# Ask the user for their age
user_age = int(input("How old are you? "))

# Determine the stage of life based on the age
if user_age < 2:
    print("You are a baby.")
elif 2 <= user_age < 4:
    print("You are a toddler.")
elif 4 <= user_age < 13:
    print("You are a kid.")
elif 13 <= user_age < 20:
    print("You are a teenager.")
elif 20 <= user_age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")
