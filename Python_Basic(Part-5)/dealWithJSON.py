import json

json_str = '{"name" : "vishal" , "age" : 23}'

student = json.loads(json_str)

print(student)
print(type(student))