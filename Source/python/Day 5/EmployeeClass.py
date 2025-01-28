# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def display_info(self):
#         print(f"The car is a {self.brand} {self.model}")
# car1=Car("Audi","Q7")
# car1.display_info()

class Employee:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary
    def allowance(self,allowance):
        self.__salary-=allowance
    def deductions(self,deductions):
        self.__salary-=deductions
    def set_salary(self,salary):
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    
salary=int(input("Enter Your Gross Salary: "))
allowances=int(input("Enter your allowances: "))
deduction=int(input("Enter Your Deductions: "))
emp=Employee("Alice",salary)
emp.deductions(deduction)
emp.allowance(allowances)
print(f"Hey {emp._Employee__name} Your Net Salary in hand is: {emp.get_salary()}")
# emp.set_salary(5000)
# print(emp.get_salary())