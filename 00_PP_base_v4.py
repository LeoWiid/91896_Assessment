import pandas as pd
import re

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

# Shows pizza menu
def show_pizza_menu():
    print('''\n
***** Pizza Menu *****
Pizza                       Regular(10 inches)     Large(14 inches)
1. Cheese Pizza                    $15                  $18
2. Hawaiian Pizza                  $18                  $22
3. Margherita Pizza                $22                  $25
4. Pepperoni Pizza                 $17                  $20
5. Meatlovers Pizza                $21                  $23
6. Chicken Supreme Pizza           $19                  $22.50
7. Crispy BBQ Pork Belly Pizza     $23                  $27
8. Seafood Pizza                   $24                  $27
9. Gluten-free Pizza               $18                  $22.50
10. Lamb Kebab Pizza               $15                  $18

Order a Maximum of 5 pizzas

******************************''')

# Shows topping menu
def show_topping_menu():
    print('''\n
***** Topping Menu *****
Extra Toppings:
1. Feta Cheese     $1.50
2. Pepperoni       $1.00
3. Mushrooms       $0.75
4. Green Peppers   $0.50
5. Black Olives    $0.75
6. Italian Sausage $1.25
7. Red Onions      $0.75
8. Spinach         $1.00
9. Bacon           $1.50
10. Tomatoes       $0.75

******************************''')

# Checks that user response is not blank
def not_blank(question, check_type="text"):
    while True:
        response = input(question)
        if response == "":
            print("Sorry this can't be blank. Please try again")
        elif check_type == "text" and not re.match("^[A-Za-z ]*$", response):
            print("Sorry, the name can only contain letters. Please try again")
        elif check_type == "numeric" and not re.match("^[0-9 ]*$", response):
            print("Sorry, the phone number can only contain numbers and spaces. Please try again")
        elif check_type == "alphanumeric" and not re.match("^[A-Za-z0-9 ]*$", response):
            print("Sorry, the address can only contain letters, numbers, and spaces. Please try again")
        else:
            return response

# Checks users enter an integer to a given question
def num_check(question):
    while True:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print("Please enter an integer")

# Checks that users enter a valid response (e.g. yes / no
# cash / credit) based on a list of options
def string_checker(question, valid_responses):
    while True:
        response = input(question).lower()
        if response in valid_responses:
            return response
        if any(response == item[:len(response)] for item in valid_responses):
            return [item for item in valid_responses if response == item[:len(response)]][0]
        print(f"Please enter a valid response from {valid_responses}")

# Currency formatting function
def currency(x):
    return "${:.2f}".format(x)

# Confirm order function
def confirm_order():
    print("Please review your order.")
    confirmation = yes_no("Do you want to confirm the order? ")
    if confirmation == "no":
        print("Order cancelled.")
        exit()
    return True

# Cash or credit function
def cash_or_credit():
    payment_method = string_checker("Would you like to pay by cash or credit? ", ["cash", "credit"])
    if payment_method == "credit":
        print("You have chosen to pay by credit.")
    else:
        print("You have chosen to pay by cash.")
    return payment_method

# Final order summary function
def print_order_summary(expense_frame, topping_frame, delivery, pizza_total, topping_total, sub_total):
    # Currency Formatting (uses currency function)
    expense_frame['Price Per Pizza'] = expense_frame['Price Per Pizza'].apply(currency)

    if delivery == "delivery":
        sub_total += 6  # Add delivery surcharge

    # Print results
    print("\nYour order summary:")
    print(expense_frame.to_string())

    print("\nYour toppings:")
    if not topping_frame.empty:
        for index, row in topping_frame.iterrows():
            if row['Toppings'] != "No extra toppings":
                for topping in row['Toppings'].split("\n"):
                    if topping.strip():  # Print topping only if it's not empty
                        print(f"  - {topping}")

    print(f"Pizzas Total Cost: {currency(pizza_total)}")
    print(f"Toppings Total Cost: {currency(topping_total)}")
    if delivery == "delivery":
        print("Delivery surcharge: $6.00")
    print(f"Total cost: {currency(sub_total)}")
    print("Thank you for your order!")

# Main routine starts here
print("Welcome to Pizza's Pitaria")

MAX_PIZZAS = 5

yes_no_list = ["yes", "no"]
delivery_option = ["delivery", "pickup"]

# Topping options as parallel lists
topping_names = ["Feta Cheese", "Pepperoni", "Mushrooms", "Green Peppers", "Black Olives",
                 "Italian Sausage", "Red Onions", "Spinach", "Bacon", "Tomatoes"]
topping_costs = [1.50, 1.00, 0.75, 0.50, 0.75, 1.25, 0.75, 1.00, 1.50, 0.75]

# List to hold pizza details
all_name = ["Cheese Pizza", "Hawaiian Pizza", "Margherita Pizza", "Pepperoni Pizza", "Meatlovers Pizza",
            "Chicken Supreme Pizza", "Crispy BBQ Pork Belly Pizza", "Seafood Pizza", "Gluten-free Pizza",
            "Lamb Kebab Pizza"]
regular_pizza_cost = [15.00, 18.00, 22.00, 17.00, 21.00,
                      19.00, 23.00, 24.00, 18.00, 15.00]
large_pizza_cost = [18.00, 22.00, 25.00, 20.00, 23.00,
                    22.50, 27.00, 27.00, 22.50, 18.00]

# Select name for order
name = not_blank("Please enter your name for the order: ")

# Ask if user wants pickup or delivery
delivery = string_checker("Do you want pickup or delivery? ", delivery_option)

if delivery == "delivery":
    print("There is a $6 surcharge")
    address = not_blank("Please enter your delivery address: ", check_type="alphanumeric")
    phone_number = not_blank("Please enter your phone number: ", check_type="numeric")

# Initialize lists to store order details
item_list = []
price_per_pizza_list = []
total_pizza_cost = 0.00
topping_item_list = []
topping_list = []
topping_price_list = []
total_topping_cost = 0.00

# Show pizza menu initially
show_pizza_menu()

# Loop to place order
while True:
    # Select pizza
    pizza_choice = num_check("Enter the pizza number (1-10): ")
    if 1 <= pizza_choice <= 10:
        pizza_name = all_name[pizza_choice - 1]
        size_choice = string_checker("Enter the size (regular/large): ", ["regular", "large"])

        if size_choice == "regular":
            price_per_pizza = regular_pizza_cost[pizza_choice - 1]
        else:
            price_per_pizza = large_pizza_cost[pizza_choice - 1]

        while True:
            quantity = num_check(f"How many {pizza_name} pizzas would you like? ")

            if quantity <= MAX_PIZZAS:
                # Calculate cost and update totals
                total_price = price_per_pizza * quantity
                item_list.append(f"{quantity}x {pizza_name} ({size_choice.capitalize()})")
                price_per_pizza_list.append(price_per_pizza)
                total_pizza_cost += total_price

                # Ask for extra toppings for each pizza ordered
                for i in range(quantity):
                    print(f"\nSelect toppings for {pizza_name} #{i+1}:")
                    extra_toppings = yes_no("Would you like extra toppings? ")
                    if extra_toppings == "yes":
                        show_topping_menu()
                        toppings = []
                        topping_cost = 0.00
                        topping_quantities = [0] * 10  # Initialize a list to store quantities for each topping

                        while True:
                            topping_choice = num_check("Enter the topping number (1-10, type 0 when finished): ")
                            if topping_choice == 0:
                                break
                            elif 1 <= topping_choice <= 10:
                                topping_quantities[topping_choice - 1] += 1  # Increment the quantity for the chosen topping
                            else:
                                print("Invalid topping choice. Please try again.")

                        # Calculate topping costs and prepare topping summary
                        for index, quantity in enumerate(topping_quantities):
                            if quantity > 0:
                                topping_name = topping_names[index]
                                topping_cost += topping_costs[index] * quantity
                                toppings.append(f"{quantity}x {topping_name}")

                        if toppings:
                            topping_summary = "\n".join(toppings)
                            topping_item_list.append(f"Toppings for {pizza_name} #{i+1}")
                            topping_list.append(topping_summary)
                            topping_price_list.append(topping_cost)
                            total_topping_cost += topping_cost
                        else:
                            topping_item_list.append(f"Toppings for {pizza_name} #{i+1}")
                            topping_list.append("No extra toppings")
                            topping_price_list.append(0.00)

                    else:
                        topping_item_list.append(f"Toppings for {pizza_name} #{i+1}")
                        topping_list.append("No extra toppings")
                        topping_price_list.append(0.00)

                break
            else:
                print(f"Please order no more than {MAX_PIZZAS} pizzas.")

        another_pizza = yes_no("Would you like to order another pizza? ")
        if another_pizza == "no":
            break

    else:
        print("Invalid pizza choice. Please choose a pizza number between 1 and 10.")

# Create dataframes to store order details
expense_data = {
    'Item': item_list,
    'Price Per Pizza': price_per_pizza_list
}

topping_data = {
    'Toppings For': topping_item_list,
    'Toppings': topping_list,
    'Topping Price': topping_price_list
}

expense_frame = pd.DataFrame(expense_data)
topping_frame = pd.DataFrame(topping_data)

# Calculate the subtotal
sub_total = total_pizza_cost + total_topping_cost

# Confirm the order
if confirm_order():
    print_order_summary(expense_frame, topping_frame, delivery, total_pizza_cost, total_topping_cost, sub_total)

# Payment method
payment_method = cash_or_credit()

# End of the order process
print("\nThank you for choosing Pizza's Pitaria. Enjoy your meal!")
