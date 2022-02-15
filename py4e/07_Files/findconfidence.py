filename = input('Enter the filename: ')
try:
    file = open(filename)
except:
    print('File', filename, 'does not exist.')
    quit()

count = 0
total = 0
for line in file:
    if line.startswith('X-DSPAM-Confidence:'):
        colon = line.find(':')
        number = line[colon + 1:].strip()
        floatnumber = float(number)
        count += 1
        total = total + floatnumber
print('Average spam confidence:', total/count)
