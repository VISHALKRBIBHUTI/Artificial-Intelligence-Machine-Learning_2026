

class Employee:

    start_time = "10am"
    end_time = "6pm"


class Teacher(Employee):

    def __init__(self , subject):
        self.subject = subject

class AdminStaff(Employee):

    def __init__(self , role):
        self.role = role



# t1 = Teacher("Maths")
# print(t1.subject , t1.start_time , t1.end_time)

adm1 = AdminStaff("Manager")
print(adm1.role , adm1.start_time , adm1.end_time)