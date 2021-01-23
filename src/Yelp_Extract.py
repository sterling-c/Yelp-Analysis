import json
import requests
import sys
import urllib
import pymongo

api_key='*****'
headers = {'Authorization': 'Bearer %s' % api_key}
url='https://api.yelp.com/v3/businesses/search'
cities = ['Los Angeles', 'San Francisco', 'Dallas',
          'Austin', 'Seattle', 'Miami', 'Boston',
          'New York City', 'Atlanta', 'Chicago']
price_levels = ['1', '2', '3', '4']
categories = 'restaurant, All'
limit = '50'
offset = '950'
sort_by = 'review_count'
json_responses = []

for city in cities:
    for price_level in price_levels:
        params = {'location': city, 'price': price_level, 'categories': categories,
                  'limit': limit, 'offset': offset, 'sort_by': sort_by}
        req = requests.get(url, params=params, headers=headers)
        print('The status code is {}'.format(req.status_code))
        json_responses.append(json.loads(req.text))
print(json_responses)


