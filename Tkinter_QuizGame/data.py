import requests

# set parameter like how many question type of question using their api
parameters = {
    # this will total question through to change just type required number
    "amount": 10,
    # type of answer boolean(True/False)
    "type": 'boolean',
}

# get question through end point
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data['results']
