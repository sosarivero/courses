from urllib.request import urlopen
import json

address = input('Enter location: ')
print(f'Retrieving {address}')
# Opens the URL
response = urlopen(address)

# Gets the data
data = response.read()
# Prints the lenth of the data for test checking purposes
print(f'Retrieved {len(data)} characters')

# Loads JSON
info = json.loads(data)

sum = 0
i = 0

# Because of the way the JSON is structured we have to index first into 'comments'
for item in info['comments']:
    # Now we can start adding up the counts and updating the counter
    sum += int(item['count'])
    i += 1


print(f'Count: {i}')
print(f'Sum: {sum}')
