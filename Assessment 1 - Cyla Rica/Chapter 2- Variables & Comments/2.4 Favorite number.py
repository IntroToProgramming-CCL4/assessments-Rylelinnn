while True:
    favorite_number = 7  #  7 favorite number

    message = f"My favorite number is {favorite_number}."
    print(message)

    # Add a way to exit the loop, for example by pressing 'q' and Enter
    user_input = input("Press 'q' and Enter to quit: ")
    if user_input == 'q':
        break