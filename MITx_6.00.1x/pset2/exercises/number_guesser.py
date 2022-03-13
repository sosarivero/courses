lowest = 0
highest = 100

guess = (highest + lowest) / 2
correct = False

print("Please think of a number between 0 and 100!")

while correct is False:
    print("Is your secret number %i?" % guess)
    feedback = input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if feedback == "c":
        correct = True
    elif feedback == "h":
        highest = guess

    elif feedback == "l":
        lowest = guess

    else:
        print("Sorry, I did not understand your input")
    guess = int((highest + lowest) / 2)


print("Game over. Your secret number was: %i" % guess)
