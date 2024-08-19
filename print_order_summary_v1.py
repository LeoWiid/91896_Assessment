# Currency formatting function
def currency(x):
    return "${:.2f}".format(x)

# Final order summary function
def print_order_summary(expense_frame, delivery, sub_total):
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