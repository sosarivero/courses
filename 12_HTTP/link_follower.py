# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Gets input from user
i = int(input('Enter count: '))
pos = int(input('Enter position: '))

# Prints the very first URL for Assignment testing purposes
print(f'Retrieving: {url}')

# Creates a loop that repeats the number of times requested by the user
for loop in range(i):
    # Updates list of anchor tags
    tags = soup('a')
    # Finds the person in the position chosen by the user
    # The position needs to be -1 because it's a zero-indexed Python list
    target = tags[pos - 1].get('href')
    # Print statement for testing purpose
    print(f'Retrieving: {target}')
    # Uses the HTTP client to open the next URL
    new_target = urllib.request.urlopen(target, context=ctx).read()
    # Makes BeautifulSoup use the URL in preparation for the next iteration
    soup = BeautifulSoup(new_target, 'html.parser')
