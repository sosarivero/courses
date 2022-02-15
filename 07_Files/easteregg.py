filename = input('Enter the filename: ')

# Define easter egg as specified by the exercise
if filename == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()
# Normal user input behavior
else:
    try:
        file = open(filename)
    except:
        print('File cannot be opened:', filename)
        quit()

count = 0
for line in file:
    count += 1

print('There were', count, 'subject lines in', filename)
