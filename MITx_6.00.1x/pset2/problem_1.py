# balance = 42
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04

for i in range(12):
    minimum_payment = balance * monthlyPaymentRate
    unpaid_balance = balance - minimum_payment
    interest = annualInterestRate/12 * unpaid_balance
    balance = unpaid_balance + interest

print('Remaining balance: %s' % str(round(balance, 2)))
