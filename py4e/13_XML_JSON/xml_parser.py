from urllib.request import urlopen
import xml.etree.ElementTree as ET

address = input('Enter location: ')
print(f'Retrieving {address}')
# Opens the URL
response = urlopen(address)

# Gets the data
data = response.read().decode()
# Prints the lenth of the data for test checking purposes
print(f'Retrieved {len(data)} characters')

# Creates a XML tree from the data
tree = ET.fromstring(data)

# Make a list with all the tags we are looking for
count_tags = tree.findall('.//count')

sum = 0
i = 0

for tag in count_tags:
    # Uses .text to access the data from each of the tags
    sum += int(tag.text)
    i += 1

print(f'Count: {i}')
print(f'Sum: {sum}')
