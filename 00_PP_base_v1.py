import pandas as pd


# Functions go here
def yes_no(question):
    while True:
        response = input(question).lower()

        if response in ("yes", "y"):
            return "yes"

        elif response in ("no", "n"):
            return "no"

        else:
            print("Please enter yes or no")

# shows menu

def show_menu():
    print('''\n
***** Menu *****
Pizza                       Regular(10 inches)     Large(14 inches)
1. Cheese Pizza                    $15                  $18
2. Hawaiian Pizza                  $18                  $22
3. Margherita Pizza                $22                  $25
4. Pepperoni Pizza                 $17                  $20
5. Meatlovers Pizza                $21                  $23
6. Chicken Supreme Pizza           $19                  $22.50
7. Crispy BBQ Pork Belly Pizza                   $23                  $27
8. Seafood Pizza                   $24                  $27
9. Gluten-free Pizza               $18                  $22.50


Extra Toppings:
1.Feta Cheese     $1.50
2.Pepperoni       $1.00
3.Mushrooms       $0.75
4.Green Peppers   $0.50
5.Black Olives    $0.75
6.Italian Sausage $1.25
7.Red Onions      $0.75
8.Spinach         $1.00
9.Bacon           $1.50
10.Tomatoes       $0.75

Order a Maximum of 5 pizzas

******************************''')

# checks that user response is not blank

def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response

# checks users enter an integer to a given question

def num_check(question):
    while True:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print("Please enter an integer")

# checks that users enter a valid response (e.g. yes / no
# cash / credit) based on a list of options

def string_checker(question, valid_responses):
    while True:
        response = input(question).lower()
        if response in valid_responses or response in [item[0] for item in valid_responses]:
            return response
        print(f"Please enter a valid response from {valid_responses}")

# currency formatting function

def currency(x):
    return "${:.2f}".format(x)


# Main routine starts here
print("Welcome to Pizza's Pitaria")

MAX_PIZZAS = 5

yes_no_list = ["yes", "no"]
delivery_option = ["delivery", "pickup"]

# List to hold pizza details
all_name = ["Cheese", "Hawaiian", "Margherita", "Pepperoni", "Meatlovers",
            "Chicken Supreme", "Crispy BBQ Pork Belly", "Lamb Kebab", "Peri Peri Chicken",
            "Chicken and Camembert"]
regular_pizza_cost = [7.00, 7.00, 7.00, 7.00, 10.00,
                    10.00, 10.00, 10.00, 15.00, 15.00]
large_pizza_cost = [10.00, 10.00, 10.00, 10.00, 13.00,
                    13.00, 13.00, 13.00, 18.00, 18.00]

# Dictionary used to create data frame ie: column_name:
pizza_order_dict = {
    "Name": all_name,
    "Regular Pizza Cost": regular_pizza_cost,
    "Large Pizza Cost": large_pizza_cost,
}

# Select name for order
name = not_blank("Please enter your name for the order: ")

# Ask if user wants pickup or delivery
delivery = string_checker("Do you want pickup or delivery? ", delivery_option)

if delivery == "delivery":
    print("There is a $6 surcharge")

# Initialize lists to store order details
item_list = []
quantity_list = []
price_list = []

# Loop to place order
while True:
    want_order = yes_no("Would you like to place an order? ")

    if want_order == "yes":
        show_menu()

        # Select pizza
        pizza_choice = num_check("Enter the pizza number (1-10): ")
        if 1 <= pizza_choice <= 10:
            pizza_name = all_name[pizza_choice - 1]
            size_choice = string_checker("Enter the size (regular/large): ", ["regular", "large"])

            if size_choice == "regular":
                price = regular_pizza_cost[pizza_choice - 1]
            else:
                price = large_pizza_cost[pizza_choice - 1]

            quantity = num_check(f"How many {pizza_name} pizzas would you like? ")

            if quantity <= MAX_PIZZAS:
                item_list.append(pizza_name)
                quantity_list.append(quantity)
                price_list.append(price * quantity)
            else:
                print(f"Sorry, you can only order up to {MAX_PIZZAS} pizzas.")
        else:
            print("Invalid pizza choice. Please try again.")

        more_pizzas = yes_no("Would you like to order more pizzas? ")
        if more_pizzas == "no":
            break
    else:
        break

# Create DataFrame
variable_dict = {
    'Item': item_list,
    'Quantity': quantity_list,
    'Price': price_list
}
expense_frame = pd.DataFrame(variable_dict)
expense_frame = expense_frame.set_index('Item')

# Calculate cost of each component
expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

# Find sub-total
sub_total = expense_frame['Cost'].sum()

# Currency Formatting (uses currency function)
add_dollars = ['Price', 'Cost']
for item in add_dollars:
    expense_frame[item] = expense_frame[item].apply(currency)

if delivery == "delivery":
    sub_total += 6  # Add delivery surcharge

# Print results
print("\nYour order summary:")
print(expense_frame)
print(f"Subtotal: {currency(sub_total)}")

print("Thank you for your order!")