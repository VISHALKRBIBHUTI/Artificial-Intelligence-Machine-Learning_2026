

import json

with open("data.json" , 'r') as f:
    student = json.load(f)


print(student)
print(type(student))