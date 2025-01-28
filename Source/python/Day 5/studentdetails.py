class Student:
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender
    def set_details(self,name,gender):
        self.__name=name
        self.__gender=gender
    def get_details(self):
        print(f"Name of the Student: {self.__name}")
        print(f"Gender : {self.__gender}")


class School(Student):
    def __init__(self, name, gender,schoolname,standard):
        super().__init__(name, gender)
        self.__schoolname=schoolname
        self.__standard=standard
    def set_details(self, name, gender,schoolname,standard):
        super().set_details(name, gender)
        self.__schoolname=schoolname
        self.__standard=standard
    def get_details(self):
        super().get_details()
        print(f"SchoolName: {self.__schoolname}")
        print(f"Standard: {self.__standard}")

class College(Student):
    def __init__(self, name, gender,collegename,branch,graduationdegree):
        super().__init__(name, gender)
        self.__collegename=collegename
        self.__branch=branch
        self.__graduationdegree=graduationdegree
    def set_details(self,name,gender,collegename,branch,graduationdegree):
        super().set_details(name,gender)
        self.__collegename=collegename
        self.__branch=branch
        self.__graduationdegree=graduationdegree
    def get_details(self):
        super().get_details()
        print(f"College Name: {self.__collegename}")
        print(f"Branch : {self.__branch}")
        print(f"graduatiodegree : {self.__graduationdegree}")


def main():
    student=Student("Jayaprakash","Male")
    student.get_details()
    student.set_details("Sam","Male")
    student.get_details()

    school=School("Jayaprakash","Male","SriBhashyam","9th")
    school.get_details()
    school.set_details("Sam","Male","StJoseph","8th")
    school.get_details()

    college=College("Jayaprakash","Male","CMRCET","CSE","UG")
    college.get_details()
    college.set_details("Sam","Male","CMRIT","CSM","PG")
    college.get_details()

if __name__=="__main__":
    main()