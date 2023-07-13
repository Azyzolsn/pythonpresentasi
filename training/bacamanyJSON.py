import json
from urllib import request

url = "https://jsonplaceholder.typicode.com/posts"

response = request.urlopen(url)

data = json.loads(response.read())

for i in range(len(data)):
    print(f"{i}. {data[i]['title']}")
    
for post in data:
    print(f"- {post['body']}")