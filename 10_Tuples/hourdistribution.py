filename = input('Enter a file name: ')
try:
    file = open(filename)
except:
    print('File', filename, 'does not exist.')
    quit()

# Creates empty dictionary
timeofday = {}

for line in file:
    # Splits lines into words
    words = line.split()
    # Guardian check from previous exercises to avoid empty lines in mbox.txt
    if len(words) < 3 or words[0] != 'From':
        continue
    # Finds the time tag and splits using the :
    hourminutes = words[5].split(':')
    # Gets the hour mark from the time tag
    hour = hourminutes[0]
    # Updates dictionary using .get()
    timeofday[hour] = timeofday.get(hour, 0) + 1

# Creates list for the tuples
tuples = list()
# Iterates through every item of the previously constructed dictionary
for time, count in timeofday.items():
    # Temporary tuple variable
    tmp = (time, count)
    # Appends to tuple list
    tuples.append(tmp)

# Sort the list
tuples = sorted(tuples)
# Print
for item in tuples:
    print(item[0], item[1])
