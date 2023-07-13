import json
file_json = open("contoh.json")

data = json.loads(file_json.read())
hobbies = data['hobbies']
print(data)

print("===================================================")
print(f"Nama : {data['name']}")
print(f"Age : {data['age']}")
print(f"City : {data['city']}")
print(f"Email : {data['email']}")
print(f"Hobbies : ")
print(f"    - {hobbies[0]}")
print(f"    - {hobbies[1]}")
print(f"    - {hobbies[2]}")
print("===================================================")
print("Address : ")
print(f"street : {data['address']['street']}")
print(f"city : {data['address']['city']}")
print(f"state : {data['address']['state']}")
print(f"zipcode : {data['address']['zipcode']}")
