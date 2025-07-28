import requests
import json
import math
import time

sleep = 1
limit = 100
all_claims = []
current_page = 1
claims_url = 'https://bitjita.com/api/claims'
user_agent = {'User-agent': 'Manserk For bitcraftmap.com'}


print('Requesting first page')
full_url = claims_url + '?limit=' + str(limit) + '&page=' + str(current_page)
data = requests.get(full_url, user_agent).json()

total_claims = int(data['count'])
total_pages = math.ceil(total_claims / limit)
all_claims.extend(data['claims'])

print('There are ' + data['count'] + ' claims to request in a total of ' + str(total_pages) + ' pages')


for page in range(total_pages-1) :
    current_page += 1
    print('sleeping for ' + str(sleep) + ' sec')
    time.sleep(sleep)
    full_url = claims_url + '?limit=' + str(limit) + '&page=' + str(current_page)
    print('Requesting page ' + full_url)
    data = requests.get(full_url, user_agent).json()
    all_claims.extend(data['claims'])

print('Total claims in array :' + str(len(all_claims)))
print('Saving into assets/data/claims.json')

with open("assets/data/claims.json", "w") as file:
    json.dump(all_claims, file)