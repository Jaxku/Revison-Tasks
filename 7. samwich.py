""""
Broken for now...
"""

# Define the prices for each ingredient
BREAD_PRICES = {'Wholemeal': 1.00, 'White': 1.00, 'Cheesy White': 1.50, 'Gluten Free': 2.00}
MEAT_PRICES = {'Chicken': 1.00, 'Beef': 0.80, 'Salami': 1.20, 'Vegan Slice': 1.40}
GARNISH_PRICES = {'Onion': 2.69, 'Tomato': 3.00, 'Lettuce': 3.30, 'Cheese': {1.69, 1.00, 2.00, 2.50}}


# Function to get the user's selection for each ingredient category
def get_selection(ingredient_prices):
    print('Please select an option:')
    for ingredient in ingredient_prices:
        print(f'{ingredient}: ${ingredient_prices[ingredient]:.2f}')
    selection = input('Enter the number corresponding to your selection: ')
    return selection


# Function to calculate the total cost of the sandwich
def calculate_cost(bread_selection, meat_selection, garnish_selection):
    cost = BREAD_PRICES[bread_selection] + MEAT_PRICES[meat_selection] + GARNISH_PRICES[garnish_selection]
    return cost


# Main program loop
while True:
    # Get the user's selection for each ingredient category
    bread_selection = get_selection(BREAD_PRICES)
    meat_selection = get_selection(MEAT_PRICES)
    garnish_selection = get_selection(GARNISH_PRICES)

    # Calculate the total cost of the sandwich
    cost = calculate_cost(bread_selection, meat_selection, garnish_selection)

    # Display the order summary
    print(f'\nYour sandwich order:')
    print(f'Bread: {bread_selection}')
    print(f'Meat: {meat_selection}')
    print(f'Garnish: {garnish_selection}')
    print(f'Total cost: ${cost:.2f}')

    # Ask the user if they want to confirm or make a change
    confirm = input('Is your order correct? (y/n): ')
    if confirm.lower() == 'y':
        print('Thank you for your order!')
        break
    else:
        print('Okay, let\'s make some changes.')
