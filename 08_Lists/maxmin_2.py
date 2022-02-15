# Creates list before loop starts:
nums = list()

while True:
    # Gets input
    user = input("Enter a number: ")
    # Finish program if user inputs done
    if user == "done":
        break
    try:
        # Convert to float in case user inputs float
        user = int(user)
        nums.append(user)

    # Exception to handle invalid input
    except:
        print("Invalid input")

print(nums)
# In a real program it'd be better to compare floats, but exercise asks int output
print("Maximum:", max(nums))
print("Minimum:", min(nums))
