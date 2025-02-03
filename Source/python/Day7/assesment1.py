from abc import ABC,abstractmethod
class Animal:
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Dog is barking!!")
class Cat(Animal):
    def make_sound(self):
        print("Cat sounds like Meow!!")
def main():
    cat=Cat()
    dog=Dog()
    cat.make_sound()
    dog.make_sound()
main()