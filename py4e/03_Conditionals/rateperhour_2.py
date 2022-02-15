try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print('Error, please enter numeric input')
    quit()

# Calculate overtime pay
if hours > 40:
    extra = hours - 40
    pay = round((40 * rate) + (extra * rate * 1.5), 2)
# Calculate regular pay if there's no overtime
else:
    pay = round(hours * rate, 2)
print('Pay:', pay)
