import json
import requests
import sys
import urllib
import pymongo

# The following information is needed to access to access the Yelp Fusion API
# The URL contains the specific endpoint used for the project, Business Search
api_key='*****'
headers = {'Authorization': 'Bearer %s' % api_key}
url='https://api.yelp.com/v3/businesses/search'

# The following are the parameters for the search endpoint.
cities = ['Los Angeles', 'San Francisco', 'Dallas',
          'Austin', 'Seattle', 'Miami', 'Boston',
          'New York City', 'Atlanta', 'Chicago']
price_levels = ['1', '2', '3', '4']
categories = 'restaurant, All'
limit = '50'
offset = '950'
sort_by = 'review_count'

json_responses = []

# This is a nested loop that creates parameters for every city listed at every price level.
# It iterates through all elements of the city list and then iterates through every price level.
for city in cities:
    for price_level in price_levels:
        params = {'location': city, 'price': price_level, 'categories': categories,
                  'limit': limit, 'offset': offset, 'sort_by': sort_by}
        # This creates and sends the request to the Yelp API and saves the results to a list.
        req = requests.get(url, params=params, headers=headers)
        print('The status code is {}'.format(req.status_code))
        json_responses.append(json.loads(req.text))
print(json_responses)


