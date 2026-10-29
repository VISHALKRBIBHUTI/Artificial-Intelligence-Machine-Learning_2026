
class Student:

    def __init__(self): # default  Constructor
        print("This is Student Class")

    def __init__(self , name , cgpa): #parametrized constructor
        self.name = name #instance attributes
        self.cgpa = cgpa #instance attributes
        print("hi")

    def get_cgpa(self): #instance method
        return self.cgpa

# stu1 = Student()
stu1 = Student("vishal" , 7.12)
print(f"name of student is : {stu1.name} and cgpa = {stu1.get_cgpa()}")

