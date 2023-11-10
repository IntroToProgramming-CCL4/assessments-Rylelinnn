#Version 2: Yellow Alien (10 points)
import random

# Generate a random alien color
alien_color = random.choice(['green', 'yellow', 'red'])

# Player's guess
player_guess = input("Guess the alien's color: ").lower()

# Force the player's guess to be the alien's color
player_guess = alien_color

# Compare player's guess with the actual alien color
if player_guess == alien_color:
    if alien_color == 'green':
        print("Congratulations! You just earned 5 points!")
    elif alien_color == 'yellow':
        print("Congratulations! You just earned 10 points!")
    elif alien_color == 'red':
        print("Congratulations! You just earned 15 points!")
    else:
        print("Invalid alien color.")
else:
    print("You're wrong. The alien's color is " + alien_color)
