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
    #by default it will print the key
    print(student)
    # to print the value we have to use the key..without separator it will print the key and value together
    print(student,students[student],sep=", ") 