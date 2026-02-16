

students = []
with open("students.csv") as file:
    for line in file:
       name,city = line.strip().split(",")
       student = {"name":name,"city":city}
       students.append(student)

#sorting by city name...can mention order by reverse flag
#sorting key is passed by lambda function
for student in sorted(students,key=lambda student: student["name"],reverse=True):
    print(f"{student["name"]} is in {student["city"]}")      