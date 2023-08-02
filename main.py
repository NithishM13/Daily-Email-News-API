import requests
from send_mail import send_email

api_key = "fa047b69a5484d60a3b2eb65c29af57b"
url = "https://newsapi.org/v2/everything?q" \
      "=tesla&sortBy=publishedAt&" \
      "apiKey=fa047b69a5484d60a3b2eb65c29af57b"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access article title and description
body = ""

for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")

send_email(body)
