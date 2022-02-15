filename = input('Enter a file name: ')
try:
    file = open(filename)
except:
    print('File', filename, 'does not exist.')
    quit()

# Creates empty dictionary
senders = {}

for line in file:
    # Splits lines into words
    words = line.split()
    # Guardian check from previous exercises to avoid empty lines in mbox.txt
    if len(words) < 3 or words[0] != 'From':
        continue
    # Updates dictionary using .get()
    senders[words[1]] = senders.get(words[1], 0) + 1

# Creates a list
count_email_list = []

# Loops with two values through the... tupples? version of the dictionary
for email, count in senders.items():
    # Creates a temporary tuple variable
    tmp = (count, email)
    # Appends tuples to list
    count_email_list.append(tmp)

# Reverses list
count_email_list = sorted(count_email_list, reverse=True)

# Sets most prolific commiter
most_prolific = count_email_list[0]

print(most_prolific[1], most_prolific[0])
