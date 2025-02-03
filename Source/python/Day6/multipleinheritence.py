class Bird:
    def __init__(self):
        pass
    def fly(self):
        return "This bird can fly."

class Mammal:
    def __init__(self):
        pass
    def walk(self):
        return "This Mammal can walk"

class Bat(Bird,Mammal):
    def __init__(self):
        super().__init__()
    def dance(self):
        return "Nattukuthu"
    
bat=Bat()
print(bat.fly())
print(bat.walk())

m1=Mammal()
m1=bat
print(m1.fly())