

import json

student = {

    "name" : "vishal",
    "age" : 23,
    "course" : "AI/ML"
}

with open("students.json" , 'w') as f:
    json.dump(student , f)