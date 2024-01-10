Ramen_menu = [
    {'code': 'A1', 'name': 'Shoyu', 'price': 10, 'category': 'ramen'},
    {'code': 'A2', 'name': 'Miso', 'price': 30, 'category': 'ramen'},
    {'code': 'A3', 'name': 'Shio', 'price': 10, 'category': 'ramen'},
    {'code': 'A4', 'name': 'Shrimp', 'price': 50, 'category': 'ramen'},
    {'code': 'A5', 'name': 'Tanmen', 'price': 20, 'category': 'ramen'},
    {'code': 'A6', 'name': 'Curry', 'price': 10, 'category': 'ramen'},
    {'code': 'A7', 'name': 'Abura', 'price': 20, 'category': 'ramen'},
    {'code': 'A8', 'name': 'Hakata', 'price': 10, 'category': 'ramen'},
    {'code': 'A9', 'name': 'Sapporo', 'price': 30, 'category': 'ramen'},
 
]
 
Noodle_menu = {
    'B1': {'code': 'B1', 'name': 'Chuka', 'price': 12, 'category': 'noodle'},
    'B2': {'code': 'B2', 'name': 'Thin', 'price': 13, 'category': 'noodle'},
    'B3': {'code': 'B3', 'name': 'Thick', 'price': 12, 'category': 'noodle'},
    'B4': {'code': 'B4', 'name': 'Somen', 'price': 12, 'category': 'noodle'},
    'B5': {'code': 'B5', 'name': 'Udon', 'price': 12, 'category': 'noodle'},
    'B6': {'code': 'B6', 'name': 'Instant', 'price': 13, 'category': 'noodle'},
    'B7': {'code': 'B7', 'name': 'Rice', 'price': 12, 'category': 'noodle'}
}
 
Toppings_menu = {
    'C1': {'code': 'C1', 'name': 'Chashu', 'price': 5, 'category': 'toppings'},
    'C2': {'code': 'C2', 'name': 'Ajitama', 'price': 4, 'category': 'toppings'},
    'C3': {'code': 'C3', 'name': 'Menma', 'price': 2, 'category': 'toppings'},
    'C4': {'code': 'C4', 'name': 'Negi', 'price': 2, 'category': 'toppings'},
    'C5': {'code': 'C5', 'name': 'Nori', 'price': 2, 'category': 'toppings'},
    'C6': {'code': 'C6', 'name': 'Moyashi', 'price': 2, 'category': 'toppings'},
    'C7': {'code': 'C7', 'name': 'Corn', 'price': 2, 'category': 'toppings'},
    'C8': {'code': 'C8', 'name': 'Wakame', 'price': 2, 'category': 'toppings'},
}
 
Drinks_menu = {
 
    'D1': {'code': 'D1', 'name': 'Tea', 'price': 4, 'category': 'beverage'},
    'D2': {'code': 'D2', 'name': 'Water', 'price': 3, 'category': 'beverage'},
    'D3': {'code': 'D3', 'name': 'Coke', 'price': 3, 'category': 'beverage'},
    'D4': {'code': 'D4', 'name': 'Sprite', 'price': 3, 'category': 'beverage'},
    'D5': {'code': 'D5', 'name': 'Fanta', 'price': 3, 'category': 'beverage'},
}

def print_menu(menu):
    print("CODE\tITEM\t\tPRICE\t\t\tCATEGORY")
    for item in menu:
        print(f"{item['code']}\t{item['name']}\t\t{item['price']}\t\t\t{item['category']}")

def print_whole_menu():
    print("---- Ramen Menu ----")
    print_menu(Ramen_menu)

    print("\n---- Noodle Menu ----")
    print_menu(Noodle_menu.values())

    print("\n---- Toppings Menu ----")
    print_menu(Toppings_menu.values())

    print("\n---- Drinks Menu ----")
    print_menu(Drinks_menu.values())
 
# Call the function to print the entire menu
print_whole_menu()
 
def calculate_total(selected_items):
    total = 0
    for item in selected_items:
        if isinstance(item, dict):
            total += item['price']
        else:
            menu, code = list(item.keys())[0], list(item.values())[0]
            if menu == Ramen_menu:
                total += next(r['price'] for r in Ramen_menu if r['code'].lower() == code.lower())
            elif menu == Noodle_menu:
                total += Noodle_menu[code]['price']
            elif menu == Toppings_menu:
                total += Toppings_menu[code]['price']
            elif menu == Drinks_menu:
                total += Drinks_menu[code]['price']
    return total
 
def vending_machine():
    print("\nWelcome to the Ramen Vending Machine!\n")

    selected_ramen_code = input("What kind of ramen would you like? Enter the code: ").upper()
    
    while selected_ramen_code not in [item['code'].upper() for item in Ramen_menu]:
        print("\n\tInvalid ramen code. Please enter a valid code.")
        selected_ramen_code = input("What kind of ramen would you like? Enter the code: ").upper()

    selected_ramen = next(item for item in Ramen_menu if item['code'].upper() == selected_ramen_code)
    selected_noodle = Noodle_menu[input("\nWhat type of noodles would you like? Enter the code: ").upper()]

    selected_toppings_choice = input("\nDo you want toppings? (yes/no): ").lower()
    selected_toppings = []

    if selected_toppings_choice == 'yes':
        selected_toppings_input = input("\nSelect your toppings. Enter the codes separated by commas: ")
        selected_toppings = [Toppings_menu[code.upper()] for code in selected_toppings_input.split(',')]

    selected_drink_code = input("\nChoose a beverage. Enter the code: ").upper()
    while selected_drink_code not in Drinks_menu:
        print("\n\tInvalid beverage code. Please enter a valid code.")
        selected_drink_code = input("Choose a beverage. Enter the code: ").upper()

    selected_drink = Drinks_menu[selected_drink_code]

    temperature = input("\nHow hot would you like it? (warm/hot): ").lower()
    while temperature not in ['warm', 'hot']:
        print("\n\tInvalid input. Please enter 'warm' or 'hot'.")
        temperature = input("How hot would you like it? (warm/hot): ").lower()

    selected_items = [selected_ramen, selected_noodle, *selected_toppings, selected_drink]
    total_amount = calculate_total(selected_items)
    print(f"\nTotal amount: ${total_amount}")

    # Validate amount paid
    while True:
        try:
            amount_paid = float(input("Insert the amount you want to pay: $"))
            if amount_paid < total_amount or amount_paid % 1 != 0:
                raise ValueError("Insufficient or invalid payment. Please enter a sufficient integer amount.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    change = amount_paid - total_amount
    print(f"Change: ${change}")

    print("\nRamen is in process. Getting heated...")
    print("Please take the ramen. Thank you! Please be careful.")

    combo_choice = input("Would you like to try our Tonkotsu Ramen Combo? (yes/no): ").lower()
    if combo_choice == 'yes':
        vending_machine()  # Restart the process for the combo

# Start the vending machine
vending_machine()

