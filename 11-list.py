students = ["amit","ayansh","sourav","rahul"]
print(students)
# above line prints output as -: ['amit', 'ayansh', 'sourav', 'rahul']

for student in students:
    print(student)

# above and below code are same but above code is more efficient and easy to understand than below code
'''
print(students[0])
print(students[1])
print(students[2])
print(students[3])
'''

# if we want to print the index of the students then we can use the below code.
for i in range(len(students)):
    print(i+1,students[i])
