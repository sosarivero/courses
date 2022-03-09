s = 'obobohobobopoboovcobobo'

bob_counter = 0

for i in range(len(s)):
    # Control case to avoid indexing in the string out of range.
    if i == len(s) - 2:
        break
    elif s[i] == "b" and s[i + 1] == "o" and s[i + 2] == "b":
        bob_counter += 1

print("Nymber of times bob occurs is: ", bob_counter)
