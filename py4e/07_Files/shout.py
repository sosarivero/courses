# Get the file handle from the user
filename = input('Enter a file name: ')
# Opens the file
try:
    file = open(filename)
except:
    print('File', filename, 'does not exist.')
    quit()

# Loops through each line in the file
for line in file:
    # First trips \n
    line = line.rstrip()
    # Then converts to upper
    line = line.upper()
    print(line)
