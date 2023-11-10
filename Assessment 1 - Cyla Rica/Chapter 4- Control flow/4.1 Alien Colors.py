import random

# Generate a random alien color
alien_color = random.choice(['green', 'yellow', 'red'])

# Player's guess
player_guess = input("Guess the alien's color: ").lower()

# Compare player's guess with the actual alien color
if player_guess == alien_color:
    if alien_color == 'red':
        print("Congratulations! You just earned 5 points!")
    else:
        print("You're right! The alien's color is " + alien_color)
else:
    print("You're wrong. The alien's color is " + alien_color)