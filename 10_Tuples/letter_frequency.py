filename = input('Enter a file name: ')
try:
    file = open(filename)
except:
    print('File', filename, 'does not exist.')
    quit()

letters = dict()

for line in file:
    # Split the line into words
    words = line.split()
    for word in words:
        word = word.lower()
        # For each letter of the word
        for i in range(len(word)):
            if word[i].isalpha() == True:
                letters[word[i]] = letters.get(word[i], 0) + 1

tuples = list()

for key, value in letters.items():
    tmp = (value, key)
    tuples.append(tmp)

tuples = sorted(tuples, reverse=True)
for item in tuples:
    print(item[1], ':', item[0])
