import requests
from send_mail import send_email

api_key = "fa047b69a5484d60a3b2eb65c29af57b"

topic = "tesla"
url = "https://newsapi.org/v2/everything?q" \
      f"={topic}&sortBy=publishedAt&" \
      "apiKey=fa047b69a5484d60a3b2eb65c29af57b&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access article title and description
body = "Subject: Today's News..."

for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] \
               + "\n" + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")

send_email(body)
