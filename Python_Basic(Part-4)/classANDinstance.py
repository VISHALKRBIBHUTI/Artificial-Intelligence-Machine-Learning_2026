
class Student:
    college_name = "ABC College" #class attribute
    PI = 3.1

    def __init__(self , name , cgpa):
        self.name = name #instance attribute
        self.cgpa = cgpa #instance attribute
        self.PI = 3.14 #instance attribute



stu1 = Student("vishal" , 7.12)
print(stu1.name)
print(stu1.cgpa)
print(stu1.college_name)
print(Student.college_name)
print(stu1.PI)
