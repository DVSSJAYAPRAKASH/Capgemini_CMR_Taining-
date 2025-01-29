import dis
class DefaultConstructor():
    def __init__(self):
        self.message="Default Constructor Called!"
    def method1(self):
        print("Method1 Called!!")

class Employee_details():
    company_name="CapG"
    def __init__(self,name,domain):
        self.name=name
        self.domain=domain

def main():
    dc=DefaultConstructor()
    dc.method1()
    print(dc.message)
    emp=Employee_details("Jayaprakash","Analyst")
    print(Employee_details.company_name)  #Static variable
    print(f"Name : {emp.name} and Role : {emp.domain}") # Instance Variable
    dis.dis(DefaultConstructor)

main()