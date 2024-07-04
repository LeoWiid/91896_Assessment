

# Functions go here

# shows menu




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


def order_price_calc


# checks that users enter a valid response (e.g. yes / no
# cash / credit) based on a list of options

def string_checker(question, num_letters, valid_response)




# currency formatting function

def currency(x):
    return "${:.2f}".format(x)


# main routine starts here