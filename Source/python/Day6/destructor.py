class Destructor:
    def __init__(self,name):
        self.name=name
        print(f"Hello Constructor Created!!{self.name}")
    def __del__(self):
        print(f"Object Constructor is Destroyed!!!")
dest=Destructor("Jp")
del dest
