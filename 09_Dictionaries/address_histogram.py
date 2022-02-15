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

# Sets a bucket to store the highest value
maximum = None
max_author = None
# Loops with two values through the... tupples? version of the dictionary
for key, value in senders.items():
    # Updates the maximum value
    if maximum == None or value > maximum:
        maximum = value
        max_author = key

print(max_author, maximum)
