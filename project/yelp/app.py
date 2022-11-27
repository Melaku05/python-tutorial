import requests
import config

url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "Authorization": "Bearer {}".format(config.Api_key)
}

params = {
    "term": "barber",
    "location": "San Francisco"

}

response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
# list comprehension
name = [business["name"]
        for business in businesses if business["rating"] > 4.5]
print(name)
