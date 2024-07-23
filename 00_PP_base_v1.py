import pandas

# Functions go here

# shows menu

def show_menu():

        print('''\n
    ***** Menu *****
    Pizza                    Regular(10 inches)     Large(14 inches)
    Margherita Pizza + Niggas  $15       $18
    Pepperoni Pizza            $18       $22
    Hawaiian Pizza             $22       $25
    Vegetarian Pizza           $17       $20
    BBQ Chicken Pizza          $21       $23
    Four Cheese Pizza          $19       $22.50
    Supreme Pizza              $23       $27
    Seafood Pizza              $24       $27
    Gluten-free Pizza          $18       $22.50


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

# Calculate the order price


def order_price_calc(var_type):


    # lists to hold ticket details
    all_names = ["a", "b", "c", "d", "e"]
    all_tickets_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
    surcharge = [0, 0, 0.53, 0.53, 0]

    mini_movie_dict = {
        "Name": all_names,
        "Ticket Price": all_tickets_costs,
        "Surcharge": surcharge
    }

    mini_movie_frame = pandas.DataFrame(mini_movie_dict)
    mini_movie_frame = mini_movie_frame.set_index('Name')

    # Calculate the total tickets cost (ticket + surcharge)
    mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                                + mini_movie_frame['Ticket Price']

    # calculate the profit for each ticket
    mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

    # calculate ticket and profit totals
    total = mini_movie_frame['Total'].sum()
    profit = mini_movie_frame['Profit'].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
    for var_item in add_dollars:
        mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

    print("---- Ticket Data ----")
    print()

    # output table with ticket data
    print(mini_movie_frame)

    print()
    print("----- Ticket Cost / Profit -----")

    # output total tickets sales and profit
    print("Total Ticket Sales: ${:.2f}".format(total))
    print("Total Profit : ${:.2f}".format(profit))


# checks that users enter a valid response (e.g. yes / no
# cash / credit) based on a list of options

def string_checker(question, num_letters, valid_responses):
    error = "Please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item




# currency formatting function

def currency(x):
    return "${:.2f}".format(x)


# main routine starts here