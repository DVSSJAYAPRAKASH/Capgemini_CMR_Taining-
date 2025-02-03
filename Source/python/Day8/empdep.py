from abc import ABC, abstractmethod
from typing import List

# Step 1: Define Employee interface using Abstract Base Class (ABC)
class Employee(ABC):
    def __init__(self, name: str, salary: float, role: str):
        self.name = name
        self.salary = salary
        self.role = role

    @abstractmethod
    def work(self) -> str:
        pass
# Step 2: Create concrete classes for different types of employees

class Manager(Employee):
    def __init__(self, name: str, salary: float):
        super().__init__(name, salary, "Manager")

    def work(self) -> str:
        return f"{self.name} is managing the team."
    
    def get_salary(self) -> float:
        return self.salary

class Developer(Employee):
    def __init__(self, name: str, salary: float):
        super().__init__(name, salary, "Developer")

    def work(self) -> str:
        return f"{self.name} is writing code."

    def get_salary(self) -> float:
        return self.salary

class Intern(Employee):
    def __init__(self, name: str, salary: float):
        super().__init__(name, salary, "Intern")

    def work(self) -> str:
        return f"{self.name} is learning and assisting."
    
    def get_salary(self) -> float:
        return self.salary

class Security(Employee):
    def __init__(self, name: str, salary: float):
        super().__init__(name, salary, "Security")

    def work(self) -> str:
        return f"{self.name} is securing the assets."
    
    def get_salary(self) -> float:
        return self.salary

# Step 3: Define Department class that manages Employees

class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees: List[Employee] = []

    def hire(self, employee: Employee) -> None:
        self.employees.append(employee)
        print(f"{employee.name} has been hired as {employee.role}.")

    def fire(self, employee: Employee) -> None:
        if employee in self.employees:
            self.employees.remove(employee)
            print(f"{employee.name} has been fired.")
        else:
            print(f"{employee.name} is not in this department.")

    def promote(self, employee: Employee, new_role: str) -> None:
        if employee in self.employees:
            old_salary = employee.salary
            employee.role = new_role  # Updating the role
            employee.salary *= 1.10  # Increasing salary by 10%
            print(f"{employee.name} has been promoted to {new_role} with a new salary of ${employee.salary:.2f} (previously ${old_salary:.2f}).")
        else:
            print(f"{employee.name} is not in this department.")

    def get_total_salary(self) -> float:
        return sum(employee.get_salary() for employee in self.employees)

    def show_employee_details(self) -> None:
        print(f"\nEmployees in {self.name} Department:")
        for employee in self.employees:
            print(f"- {employee.name}, Salary: ${employee.get_salary():.2f}, Role: {employee.role}, Work: {employee.work()}")

# Step 4: Create department and add employees

# Create employees
manager = Manager("Alice", 80000)
developer = Developer("Bob", 60000)
intern = Intern("Charlie", 20000)
security_staff = Security("Ram", 5000)

# Create a department and hire employees
it_department = Department("IT")

it_department.hire(manager)
it_department.hire(developer)
it_department.hire(intern)
it_department.hire(security_staff)

# Show employee details before promotion
it_department.show_employee_details()

# Promote an employee (Security staff to Security Manager)
it_department.promote(security_staff, "Security Manager")

# Show updated employee details after promotion
it_department.show_employee_details()

# Total salary in the department
total_salary = it_department.get_total_salary()
print(f"\nTotal salary expense for {it_department.name} department: ${total_salary:.2f}")
