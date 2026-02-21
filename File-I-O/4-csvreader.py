import csv

students = []

with open("students.csv") as file:
    # The DictReader class reads the CSV file and maps the information into a dictionary using the header row as keys.
    # The CSV file needs to have a header row with the column names (e.g., "name,city") for this to work correctly.
    reader = csv.DictReader(file)

    # The default csv reader approach
    #reader = csv.reader(file)
    # for row in reader:
    #     students.append({"name": row[0],"city": row[1]})

    # below approach is to use if we know mapping 
    # for name,city in reader:
    #     students.append({"name": name,"city": city})
    for row in reader:
        students.append({"name":row["name"],"city":row["city"]})


    
for student in sorted(students,key=lambda student: student["name"],reverse=True):
    print(f"{student["name"]} is in {student["city"]}")   