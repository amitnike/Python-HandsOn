#use of class
class Student:
    ...

def main():
    #name = get_name()
    #house = get_house()
    #print(f"{name} from {house}")
    
    #n,h = get_student()
    #print(f"{n} from {h}")

    #use of tuple..they are immutable in nature
    # student = get_student()
    # print(f"{student[0]} from {student[1]}")

    # use of list
    # student = get_student_aslist()
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"
    # print(f"{student[0]} from {student[1]}")

    #use of dict..also add single quotes while accessing the student name and house
    # student = get_student_asdict()
    # print(f"{student['name']} from {student['house']}")

    student = get_student_obj()
    print(f"{student.name} from {student.house}") 

def get_name():
    return input("Name:" )

def get_house():
    return input("House:" )

# def get_student():
#     name = input("Name:" )
#     house = input("House:" )
#     return name,house

# use of tuple
def get_student():
    name = input("Name:" )
    house = input("House:" )
    return (name,house)

#use of list , instead of tuple..as list is mutable
def get_student_aslist():
    name = input("Name:" )
    house = input("House:" )
    return [name,house]

#use of dict
def get_student_asdict():
    #initialize empty dictionary
    student = {}
    student["name"] = input("Name:" )
    student["house"] = input("House:" )
    return student

def get_student_obj():
    student = Student()
    student.name = input("Name:" )
    student.house = input("House:" )
    return student


if __name__ == "__main__":
    main()