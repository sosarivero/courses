import urllib.request
import urllib.parse
import urllib.error
import json
import ssl


serviceurl = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    # Need to create a dictionary with the keys 'address' and 'key' because that's how the API works.
    dictionary = dict()
    dictionary['address'] = address
    dictionary['key'] = api_key
    # Creates the URI with the address and key query
    url = serviceurl + urllib.parse.urlencode(dictionary)

    print('Retrieving', url)
    # Opens the query
    json_file = urllib.request.urlopen(url)
    # Reads and decodes it
    data = json_file.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        # Use the JSON handler to read it
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # Print the 'place id' from the results handed in by the API
    location = js['results'][0]['place_id']
    print(f'Place id {location}')
