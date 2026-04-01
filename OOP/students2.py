#use of class
class Student:
    #constructor
    #None to pass optional value
    def __init__(self,name,house,patronus=None):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["wai","pune","baramati"]:
            raise ValueError("Invalid House")     
        self.name = name
        self.house = house
        self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} from {self.house} uses {self.patronus}"
    
    #custom method
    def charm(self):
        if self.patronus == "stag":
            return "Stupefy"
        elif self.patronus == "otter":
            return "Expelliarmus"
        else:
            return "Riddikulus"

#main method
def main():
    student = get_student_obj()
    print(f"{student.name} from {student.house}") 
    #below to work...need to update Student class else it will print the address
    print(student)
    #call the charm method
    print(student.charm())

def get_student_obj():
    name = input("Name:" )
    house = input("House:" )
    patronus = input("Patronus:" )
    #constructor call
    return Student(name,house,patronus)


if __name__ == "__main__":
    main()