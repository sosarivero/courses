count = 0
sum = 0
while True:
    user = input("Enter a number: ")
    if user == "done":
        break
    try:
        user = float(user)
        sum = sum + user
        count += 1
    except:
        print("Invalid input")

avg = sum / count
print(sum, count, avg)
