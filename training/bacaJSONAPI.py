import json
from urllib import request

url = "https://api.github.com/users/ardianta"

response = request.urlopen(url)

data = json.loads(response.read())

print(data)