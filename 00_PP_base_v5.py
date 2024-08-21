import pandas
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
def not_blank(question):
    while True:
        response = input(question)
        if response == "":
            print("Sorry this can't be blank. Please try again")
        elif not re.match("^[A-Za-z ]*$", response):
            print("Sorry, the name can only contain letters. Please try again")
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
        if response in [item[0] for item in valid_responses]:
            return valid_responses[[item[0] for item in valid_responses].index(response)]
        print(f"Please enter a valid response from {valid_responses}")


# Currency formatting function
def currency(x):
    return "${:.2f}".format(x)


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
all_name = ["Cheese", "Hawaiian", "Margherita", "Pepperoni", "Meatlovers",
            "Chicken Supreme", "Crispy BBQ Pork Belly", "Seafood", "Gluten-free",
            "Lamb Kebab"]
regular_pizza_cost = [15.00, 18.00, 22.00, 17.00, 21.00,
                      19.00, 23.00, 24.00, 18.00, 15.00]
large_pizza_cost = [18.00, 22.00, 25.00, 20.00, 23.00,
                    22.50, 27.00, 27.00, 22.50, 18.00]

pizza_menu = {
    "Pizza": all_name,
    "Regular(10 inches)": regular_pizza_cost,
    "Large": large_pizza_cost
}

# Select name for order
name = not_blank("Please enter your name for the order: ")

# Ask if user wants pickup or delivery
delivery = string_checker("Do you want pickup or delivery? ", delivery_option)

if delivery == "delivery":
    print("There is a $6 surcharge")

# Initialize lists to store order details
item_list = []
price_per_pizza_list = []
total_pizza_cost = 0.00
topping_item_list = []
topping_list = []
topping_price_list = []
total_topping_cost = 0.00

# Show pizza menu initially
full_pizza_menu = pandas.DataFrame(pizza_menu)
full_pizza_menu.index += 1
print(full_pizza_menu)
#show_pizza_menu()

# Loop to place order
while True:
    # Select pizza
    print()
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

                # Handle toppings for each individual pizza
                for _ in range(quantity):
                    print(f"\nAdding toppings for a {pizza_name} ({size_choice.capitalize()}) pizza.")
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

                        # Calculate topping costs and prepare topping details
                        for index, quantity in enumerate(topping_quantities):
                            if quantity > 0:
                                topping_name = topping_names[index]
                                topping_price = topping_costs[index]
                                topping_cost += topping_price * quantity
                                toppings.append(f"{topping_name} (+{currency(topping_price * quantity)})")

                        topping_item_list.append(f"{pizza_name} ({size_choice.capitalize()})")
                        topping_list.append("\n".join(toppings) if toppings else "No extra toppings")
                        topping_price_list.append(topping_cost)  # Calculate the total topping cost for this pizza
                        total_topping_cost += topping_cost  # Update total topping cost
                    else:
                        topping_item_list.append(f"{pizza_name} ({size_choice.capitalize()})")
                        topping_list.append("No extra toppings")
                        topping_price_list.append(0.00)

                break  # Exit the quantity loop

            else:
                print(f"Sorry, you can only order up to {MAX_PIZZAS} pizzas. Please enter a valid number.")

    else:
        print("Invalid pizza choice. Please try again.")

    # Ask if user wants to order more pizzas and show the menu again if they do
    more_pizzas = yes_no("Would you like to order more pizzas? ")
    if more_pizzas == "yes":
        show_pizza_menu()  # Show pizza menu again for the next order
    else:
        break

# Create DataFrame for pizzas
expense_frame = pd.DataFrame({
    'Item': item_list,
    'Price Per Pizza': price_per_pizza_list
})
expense_frame = expense_frame.set_index('Item')

# Create DataFrame for toppings
topping_frame = pd.DataFrame({
    'Pizza': topping_item_list,
    'Toppings': topping_list
})
topping_frame = topping_frame.set_index('Pizza')

# Print the final order summary
print_order_summary(expense_frame, topping_frame, delivery, total_pizza_cost, total_topping_cost,
                    total_pizza_cost + total_topping_cost)
