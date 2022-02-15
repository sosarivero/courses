filename = input('Enter a file name: ')
try:
    file = open(filename)
except:
    print('File', filename, 'does not exist.')
    quit()

# Creates empty dictionary
weekdays = {}

for line in file:
    # Splits lines into words
    words = line.split()
    # Guardian check from previous exercises to avoid empty lines in mbox.txt
    if len(words) < 3 or words[0] != 'From':
        continue
    # Updates dictionary using .get()
    weekdays[words[2]] = weekdays.get(words[2], 0) + 1

print(weekdays)
