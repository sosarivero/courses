# balance = 999999
# annualInterestRate = 0.18

# Creates a temporary variable with same value as the balance
tmp = balance
monthly_interest = annualInterestRate / 12.0
# The initial lower bound for the binary search is one-twelfth of the original balance.
lower = balance / 12
# The upper bound is a one-twelfth of the balance, after having its interest compounded after a year.
upper = (balance * (1 + monthly_interest)**12) / 12.0

# Loops until a payment is found that is able to make balance reach 0 after a year.
# Need to round in order to avoid the infinite loop.
while round(tmp, 1) != 0:
    # After each failed payment test, resets the balance and updates the payment guess
    tmp = balance
    payment = (lower + upper) / 2
    # Calculates the balance in a year...
    for i in range(12):
        # ... using the fixed testing payment per month.
        unpaid_balance = tmp - payment
        tmp = unpaid_balance + unpaid_balance * monthly_interest
    # Updating the lower and upper bounds for the binary search
    if tmp > 0:
        lower = payment
    elif tmp < 0:
        upper = payment

print("Lowest Payment: %s" % str(round(payment, 2)))
