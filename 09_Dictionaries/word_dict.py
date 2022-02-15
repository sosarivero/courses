file = open('words.txt')

word_list = dict()

for line in file:
    print(line)
    words = line.split()
    for word in words:
        word_list[word] = word_list.get(word, 0)

check = input('What word do you want to check if is in the text? ')
print(check in word_list)
