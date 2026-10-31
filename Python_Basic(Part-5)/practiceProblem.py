with open("sample.txt", "w+") as f:
    f.write("This is a sample file\n"
            "which store some words\n"
            "for Python Activity\n"
            "which is search by us")

    f.seek(0)

    data = f.read()

    print(data)

    isFound = data.find("Python")

    if isFound != -1:
        print("Python exists in file")
    else:
        print("Python Not Exist in File")