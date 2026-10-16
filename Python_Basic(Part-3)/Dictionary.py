

info = {

    "name" : "vishal",
    "age":23,
    3.14 : "PI",
    "country":"India"
}

# print(type(info))
# print(info["name"])
# print(info["age"])
# print(info[3.14])

# 1. dict.key()
print(info.keys())

print()

# 2. dict.values()
print(info.values())

print()

# 3. dict.items()
print(info.items())

print()

# 4. dict.get()
print(info.get("name"))
print(info.get("hi" , "Not Found"))

print()

# 5. dict.update()
print(info.update({"fruits" : "Apple"}))

print()

print(info.items())


