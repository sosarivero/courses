#  List all unique words, sorted in alphabetical order

filename = input('Enter file: ')

try:
    file = open(filename)
except:
    print('Invalid file')
    quit()

unique_words = list()

# Loop through each line in file
for line in file:
    # Creates list of words in line
    words = line.split()
    # Nested loop
    for word in words:
        if word in unique_words: continue
        # Append unique word
        unique_words.append(word)

unique_words.sort()
print(unique_words)