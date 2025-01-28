class Parent:
    def __init__(self):
        self.bignose="7cm"
        print("Parent Constructor")
    def display_parent(self):
        print("This is Parent Class")
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")
    def display_child(self):
        print("This is Child Class")

child=Child()
child.display_child()
print(child.bignose)