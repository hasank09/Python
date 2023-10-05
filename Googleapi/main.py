# Python
import pandas as pd
import requests
import time

API_KEY = 'Use Your API Key'
SEARCH_ENGINE_ID = 'Use her Search Engine I'


def build_payload(query, start=1, num=0, dateRestrict='m1', **params):
    pay_load = {

        'key': API_KEY,
        'q': query,
        'cx': SEARCH_ENGINE_ID,
        'start': start,
        'num': num,
        'dateRestrict': dateRestrict,
    }
    pay_load.update(params)
    return pay_load


def make_request(payload):
    response = requests.get(url='https://customsearch.googleapis.com/customsearch/v1', params=payload)
    if response.status_code != 200:
        print(response.status_code)
        print(response.text)
        raise Exception('Request Failed')
    print(str(payload['start']) + '>>>>' 'Okay')
    return response.json()


# For Website title
website_title = []
# For Website Link
website_links = []

for i in range(10):
    start_index = i*10 +1
    # for Customize Search "https://www.exploit-db.com/google-hacking-database"
    query_set = 'site:.ch intitle:restaurant'

    new_payload = build_payload(query=query_set, start=start_index)
    data = make_request(payload=new_payload)
    print(data)
    all_results = data['items']
    for result in all_results:
        website_title.append(result['title'])
        website_links.append(result['link'])

    # To avoid frequent request
    time.sleep(2)

final_results = {
    'restaurant_name': website_title,
    'website': website_links,
}

df = pd.DataFrame.from_dict(data=final_results)

df.to_csv('result_swiz.csv')

final_results.clear()
