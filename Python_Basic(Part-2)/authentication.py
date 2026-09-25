
username = input("Enter UserName : ")
password = input("Enter Password : ")


if(username == "admin"  and password == "pass"):
    print("LogIn Sucessfull!")
else:
    if(username == "admin"):
        print("Wrong password")
    else:
        print("Wrong username")
