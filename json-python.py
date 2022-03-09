# write a python program to convert json to python

import json

x = {"fname": "nalamothu", "lname": "pravallika", "age": 22, "city": "ongole"}

print("the json data is:\n", x)
y = json.dumps(x)
z = json.loads(y)
print("the loads is:", z)
print(z["age"])
print(z["fname"])
print(z["city"])
