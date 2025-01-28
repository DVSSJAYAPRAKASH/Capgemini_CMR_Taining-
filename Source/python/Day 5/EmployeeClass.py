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
salary//=12
medicalallowances=int(input("Enter your Medical allowances: "))
medicalallowances//=12
travelallowances=int(input("Enter your Travel allowances: "))
travelallowances//=12
allowances=medicalallowances+travelallowances
pfdeduction=int(input("Enter Your PF Deductions: "))
pfdeduction//=12
tdsdeduction=int(input("Enter Your TDS Deductions: "))
tdsdeduction//=12
deduction=pfdeduction+tdsdeduction
emp=Employee("Alice",salary)
emp.deductions(deduction)
emp.allowance(allowances)
print(f"Hey {emp._Employee__name} Your Net Salary in hand is: {emp.get_salary()}")
# emp.set_salary(5000)
# print(emp.get_salary())