# %%

import requests
from pprint import pprint

# https://api.stackexchange.com/docs

response = requests.get('https://api.stackexchange.com/docs')

print(response.status_code)


# %% 10 Most Highly Voted Posts

data = {
    "site": 'stackoverflow',
    "fromdate": '1633996800',
    "todate": '1634083200',
    "order": 'desc',
    "sort": 'votes',
    "pagesize": '10'
}

response = requests.get("https://api.stackexchange.com/2.3/posts", params=data).json()

# print(response.status_code)
# pprint(response)

for n in range(len(response["items"])):
    print(response["items"][n]["score"])


# %% Badges


data = {
    "site": 'stackoverflow',
    "order": 'asc',
    "sort": 'name',
    "pagesize": '3'
}

response = requests.get("https://api.stackexchange.com/2.3/badges", params=data).json()

pprint(response)


# %% Badges Part 2

badge_ids = [9878, 204, 600]

data = {
    "site": 'stackoverflow',
    "pagesize": '1'
}

for id in badge_ids:
    url = f"https://api.stackexchange.com/2.3/badges/{id}/recipients"
    response = requests.get(url, params=data).json()
    pprint(response)


# %% First 5 Pages DAN


def get_posts():
    
    data = {
        "site": 'stackoverflow',
        "fromdate": '1633046400',
        "todate": '1634083200',
        "order": 'asc',
        "sort": 'activity',
        "pagesize": '5',
        #"page": '5',
        #"has_more": False
    }

    page_number = 1

    posts = []

    response = requests.get("https://api.stackexchange.com/2.3/posts", params=data).json()

    while page_number < 6 and response["has_more"] == True:
        data["page"] = str(page_number)
        response
        page_number += 1
        posts.append(response["items"])
    return posts

get_posts()

#pprint(response)


# %%

data = {
    "site": 'stackoverflow',
    "fromdate": '1633046400',
    "todate": '1634083200',
    "order": 'desc',
    "sort": 'votes',
    "pagesize": '5',
    #"page": '5',
}