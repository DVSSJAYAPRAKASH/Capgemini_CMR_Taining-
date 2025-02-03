from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def display(self):
        pass
    def show(self):
        print("Concrete Class")
class Son(Father):
    def display(self):
        print("Son is implementing the abstract method")
class Daughter(Father):
    def display(self):
        print("Daughter is implementing the abstract method")
def main():
    son=Son()
    son.display()
    son.show()
    d=Daughter()
    d.display()
    d.show()
main()