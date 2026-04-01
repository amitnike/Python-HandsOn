#use of class
class Student:
    #constructor
    def __init__(self,name,house):
        #do not add _ as added in setter method            
        self.name = name
        self.house = house

    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    #getter
    @property
    def house(self):
        return self._house

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name
    
    #setter...decorator function
    @house.setter
    def house(self,house):
        if house not in ["wai","pune","baramati"]:
            raise ValueError("Invalid House")
        self._house = house

#main method
def main():
    student = get_student_obj()
    #below line will throw excpetion as per the logic in the setter method
    #student.house = "mumbai"
    #below to work...need to update Student class else it will print the address
    print(student)


def get_student_obj():
    name = input("Name:" )
    house = input("House:" )
    #constructor call
    return Student(name,house)


if __name__ == "__main__":
    main()