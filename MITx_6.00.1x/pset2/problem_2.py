# balance = 3329
# annualInterestRate = 0.2

# Creates a temporary variable with same value as the balance
tmp = balance
payment = 0

# Loops until a payment is found that is able to make balance reach 0 after a year
while tmp > 0:
    # After each failed payment test, resets the balance and adds $10 to the payment
    tmp = balance
    payment += 10
    # Calculates the balance in a year...
    for i in range(12):
        monthly_interest = annualInterestRate / 12.0
        # ... using the fixed testing payment per month.
        unpaid_balance = tmp - payment
        tmp = unpaid_balance + unpaid_balance * monthly_interest


print("Lowest Payment: %i" % payment)
