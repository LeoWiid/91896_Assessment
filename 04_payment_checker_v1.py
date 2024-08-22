# functions go here
def cash_credit(question):

    while True:
        response = input(question).lower()

        if response == "cash" or response == "ca":
            return "cash"

        if response == "credit" or response == "cr":
            return "credit"

        else:
            print("Please choose a valid payment method")


# main routine goes here
while True:
    payment_method = cash_credit("Choose a payment method (cash"
                                 "or credit): ")

    print("you chose", payment_method)
