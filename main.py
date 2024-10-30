import requests
import sendemail
api_key="3c09cc7910db479a926b79432100e6c5"

url = "https://newsapi.org/v2/everything?q=tesla" \
      "&from=2024-09-30&sortBy=publishedAt&apiKe" \
      "y=3c09cc7910db479a926b79432100e6c5"

request = requests.get(url)
content = request.json()
message = ""
for article in content["articles"]:
    if article["title"] is not None and article["description"] is not None:
        message = message + article["title"] + "\n" + article["description"] + "\n\n"

message=message.encode("utf-8")
sendemail.send_email(message)