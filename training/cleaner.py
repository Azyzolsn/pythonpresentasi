import json
file_json = open("y.json")

data = json.loads(file_json.read())

for i in range(len(data)):
    print(f"{i}. {data[i]['title']}\n{data[i]['price']}\n{data[i]['availability']}")

