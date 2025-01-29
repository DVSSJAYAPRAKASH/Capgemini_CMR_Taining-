class Employee:
    def __init__(self):
        name,sacdlary,deductions,allowance=self.take_input()
        self.__name=name
        self.__salary=salary
        self.__salary-=deductions
        self.__salary-=allowance
    def take_input(self):
        name=(input("Enter Employee Name: "))
        salary=int(input("Enter Employee Salary: "))
        deductions=int(input("Enter your deductions: "))
        allowance=int(input("Enter your total allowances: "))
        return name,salary,deductions,allowance
    def get_salary(self):
        print(f"Your Inhand Salary : {self.__salary}")


class Student:
    school_name="CMR International School"
    def __init__(self):
        self.__name,self.__gender=self.set_input()
    def set_input(self):
        name=input("Enter Student Name: ")
        gender=input("Enter Student Gender: ")
        return name,gender
    def get_details(self):
        print()
        print(f"Name of the Student: {self.__name}")
        print(f"Gender : {self.__gender}")
        print(f"School name: {Student.school_name}")



def main():

    n=int(input("Enter No.of Students Records: "))
    value=int(input("Enter No.of Employee details: "))
    list_a=[]
    list_b=[]
    for i in range(n):
        list_a.append(Student())
    for st in list_a:
        st.get_details()
    for i in range(value):
        list_b.append(Employee())
    for emp in list_b:
        emp.get_salary()

main()
    