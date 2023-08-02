import requests

api_key = "fa047b69a5484d60a3b2eb65c29af57b"
url = "https://newsapi.org/v2/everything?q" \
      "=tesla&sortBy=publishedAt&" \
      "apiKey=fa047b69a5484d60a3b2eb65c29af57b"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access article title and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
