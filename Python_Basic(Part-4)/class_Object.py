
class Student:
    # subject = "Python"
    # college = "ABC"
    # year = "4th Year Student"

    def __init__(self , name , cgpa): #constructor
        self.name = name
        self.cgpa = cgpa



stu1 = Student("vishal" , 7.12)
stu2 = Student("Rohit" , 8.9)

print(stu1.name , stu1.cgpa)


# 
print(stu2.name , stu2.cgpa)
