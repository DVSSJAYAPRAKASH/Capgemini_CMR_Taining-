import csv

class Employee:
    def __init__(self):
        self.name = input("Enter the name: ")
        self.salary = input("Enter the Salary: ")
        self.dept = input("Enter the departmentId: ")
        self.experience = input("Enter Your Experience in the Field: ")

    def getsalarydetails(self):
        return self.salary

    def getdeptdetails(self):
        return self.dept

    def getexperience(self):
        return self.experience

    def getname(self):
        return self.name

def main():
    employees = []
    n=int(input("Enter How many Records to be Stored: "))
    for i in range(n):
        emp = Employee()
        employees.append(emp)

    with open('employee_details.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Salary', 'Department', 'Experience'])
    
        for emp in employees:
            writer.writerow([emp.getname(), emp.getsalarydetails(), emp.getdeptdetails(), emp.getexperience()])

main()
