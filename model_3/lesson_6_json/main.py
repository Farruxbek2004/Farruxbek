import json
import requests

KEY = "gKOeS2ZI3wK4zTeGcKeZ8dgBp9psidFl1ntV2cAR"
url = f"https://api.freecurrencyapi.com/v1/latest?apikey={KEY}"
resp = requests.get(url)

with ollpen("weather.json", "w") as f:
    json.dump(json.loads(resp.text), f)

urll = f"https://kun.uz/news/list"

computers = [
    {
        "id": 1,
        "name": "Aser",
        "color": "yellow"
    },

    {
        "id": 2,
        "name": "Mac",
        "color": "green"
    },

    {
        "id": 3,
        "name": "HP",
        "color": "black"
    }
]

# json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
# arr = json.dumps(computers)
#
#
# with open("computers.json", "w") as f:
#     json.dump(computers, f, sort_keys=False)
#
#
# print(json.loads(arr))
#
# with open("computers.json") as f:
#     computers = json.load(f)
#
# print(computers)


# JSON  Python
# object dict
# array list
# string str
# number(int)  int
# number(real)  float
# true  True
# false  False
# null None
