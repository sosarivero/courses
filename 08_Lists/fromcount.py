
filename = input('Enter a file name: ')
file = open(filename)

count = 0
for line in file:
    if not line.startswith('From') or line.startswith('From:'):
        continue
    words = line.split()
    print(words[1])
    count += 1

print('There were', count, 'lines in the file with From as the first word')
