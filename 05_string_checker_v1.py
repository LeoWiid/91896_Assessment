def string_checker(question, valid_responses):
    while True:
        error = f"Please enter a valid response from {valid_responses}"
        response = input(question).lower()

        for item in valid_responses:
            if item == response or response == item[:2]:
                return item
        print(error)

#Main Routine

payment_option = ["cash", "credit"]

payment_method = string_checker("How would you like to pay (cash/credit)? ", payment_option)

print(f"Thank you! Your order has been confirmed. You will pay with {payment_method}.")