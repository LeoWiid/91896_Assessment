# Stops users from entering a non valid name
def name_check(question):
    while True:
        response = input(question).strip()
        if response == "" or not response.isalpha():
            print("Sorry, please enter a name using only letters.")
        else:
            return response

name = name_check("Please enter your name for the order: ")