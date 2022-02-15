filename = input('Enter a file name: ')
try:
    file = open(filename)
except:
    print('File', filename, 'does not exist.')
    quit()

# Creates empty dictionary
domains = {}

for line in file:
    # Splits lines into words
    words = line.split()
    # Guardian check from previous exercises to avoid empty lines in mbox.txt
    if len(words) < 3 or words[0] != 'From':
        continue
    # Splits the word using '@' as delimiter
    email = words[1].split('@')
    # Updates dictionary using .get(). It's email[1] as the second element of split emails will be the domain
    domains[email[1]] = domains.get(email[1], 0) + 1

print(domains)
