

class Teacher:
    def __init__(self , salary):
        self.salary = salary

class Student:
    def __init__(self , gpa):
        self.gpa = gpa

class TA(Teacher , Student):
    def __init__(self , subject , salary , gpa):
        self.subject = subject
        super().__init__(salary)
        Student.__init__(self , gpa)



ta1 = TA("Maths" , 20_000 , 7.13)
print(ta1.subject)
print(ta1.salary)
print(ta1.gpa)
print(TA.mro())