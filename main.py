import requests
from send_email import send_email

topic = "tesla"
api = "c2651126696a46999c8ac7c8ac8b7be8"

url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&apiKey=c2651126696a46999c8ac7c8ac8b7be8&" \
      "language=en"

# Make Request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
# Access the article title and description
body = ''
for article in content['articles'][:20]:
    if article["title"] is not None:
        body = body + article['title'] + '\n' + article["description"] + '\n' + article["url"] + 2*'\n'

mess = f"""\
Subject: Hi Here's Your Daily News

{body}
"""
mess = mess.encode("utf-8")
send_email(message=mess)