class Example:
    def __init__(self,*args):
        if len(args)==1:
            print(args[0])
        elif len(args)==2:
            print(args[0]+args[1])
class Example2:
    def __init__(self,clgname,**kwargs):
        self.clgname=clgname
        if "name" in kwargs and "age" in kwargs:
            print(f"Hello {kwargs['name']}, you are {kwargs['age']} years old")
        elif "name" in kwargs:
            print(f"Hello {kwargs['name']}")
        self.xfield=kwargs['name']
        
def main():
    ex=Example("Hello","World")
    obj1=Example2("CMRIT",name="JP",age=21)
    obj2=Example2("CMRCET",name="JP") 
    print(obj2.xfield)       
main()

