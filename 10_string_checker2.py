def string_checker2(question, valid_responses):
    while True:
        error = f"Please enter a valid response from {valid_responses}"
        response = input(question).lower()

        for item in valid_responses:
            if item == response or response == item[0]:
                return item
        print(error)

#Main Routine

size_option = ["regular", "large"]

size_pizza = string_checker2("What size would you like? (regular/large): ", size_option)
