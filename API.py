import requests

url = "https://busan-food.openapi.redtable.global/api/food/list"
headers = {
    "X-API-KEY": "jmnrNQThHqdERlP2bX1zteMJr7XiykNjfwkB00sYMFNpovUjzefzP1WVC1DsbtUB"
}
params = {
    "district": "해운대구",
    "page": 1,
    "perPage": 5
}

response = requests.get(url, headers=headers, params=params)
print(response.status_code)
print(response.json())
