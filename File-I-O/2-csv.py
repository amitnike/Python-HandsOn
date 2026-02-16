# with open("students.csv") as file:
#     for line in file:
#         #row = line.strip().split(",")
#         # make it more readable
#         name,city = line.strip().split(",")
#         #print(f"{row[0]} is in {row[1]}")
#         print(f"{name} is in {city}")



# students = []
# with open("students.csv") as file:
#     for line in file:
#        name,city = line.strip().split(",")
#        students.append(f"{name} is in {city}") 

# #sorting the result alphabetically using sorted
# for student in sorted(students):
#     print(student)

students = []
with open("students.csv") as file:
    for line in file:
       name,city = line.strip().split(",")

    #    student = {}
    #    student["name"] = name
    #    student["city"] = city
    #    students.append(student)

    #  simplified version of above code
       student = {"name":name,"city":city}
       students.append(student)

def get_city(student):
    return student["city"]

def get_name(student):
    return student["name"]

#sorting by city name...can mention order by reverse flag
#sorting key is passed as function name which gives the city name
for student in sorted(students,key=get_city,reverse=True):
    print(f"{student["name"]} is in {student["city"]}")      