import requests
api_key="3c09cc7910db479a926b79432100e6c5"

url = "https://newsapi.org/v2/everything?q=tesla" \
      "&from=2024-09-30&sortBy=publishedAt&apiKe" \
      "y=3c09cc7910db479a926b79432100e6c5"

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])