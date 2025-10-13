students =[
    {"name":"amit","add":"pune","job":"hsbc"},
    {"name":"ayansh","add":"mumbai","job":"infy"},
    {"name":"supriya","add":"hadapsar","job":"tcs"},
    {"name":"test","add":"kharadi","job":None}
]


for student in students:
    print(student["name"],student["add"],student["job"],sep=",")