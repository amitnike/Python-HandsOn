students = {
    "amit":"wai",
    "sagar":"pune",
    "ram":"mumbai",
    "sham":"nagpur"
}

'''
print(students["amit"])
print(students["sagar"])
'''

for student in students:
    print(student,students[student],sep=", ")