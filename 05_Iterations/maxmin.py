max = None
min = None

while True:
    # Gets input
    user = input("Enter a number: ")
    # Finish program if user inputs done
    if user == "done":
        break

    try:
        # Convert to float in case user inputs float
        user = float(user)
        # Case for the very first iteration of the loop
        if max == min == None:
            max = min = user
        # Cases for the next iterations
        elif user > max:
            max = user
        elif user < min:
            min = user
        # Continues program if none of the values are updated
        else:
            continue
    # Exception to handle invalid input
    except:
        print("Invalid input")

# In a real program it'd be better to compare floats, but exercise asks int output
print("Maximum is", int(max))
print("Minimum is", int(min))
