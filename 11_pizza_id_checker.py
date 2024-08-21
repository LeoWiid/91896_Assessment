def pizza_id_checker(id):
    pizza_dict = {
        1: "Cheese", 2: "Hawaiian", 3: "Margherita", 4: "Pepperoni", 5: "Meatlovers",
        6: "Chicken Supreme", 7: "Crispy BBQ Pork Belly", 8: "Lamb Kebab",
        9: "Peri Peri Chicken", 10: "Chicken & Camembert"
    }
    return pizza_dict.get(id, "Unknown Pizza")

def num_check(question, min_value=None, max_value=None):
    while True:
        try:
            response = int(input(question))
            if (min_value is not None and response < min_value) or (max_value is not None and response > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
            else:
                return response
        except ValueError:
            print("Please enter an integer.")

#Main Routine

user_order_id = num_check("Please enter the number of the pizza you want to order (1-10): ", min_value=1, max_value=10)
user_order_name = pizza_id_checker(user_order_id)

print(f"You have selected {user_order_name}")