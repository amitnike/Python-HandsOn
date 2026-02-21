import csv

name = input("what is your name ?")
city = input("where do you live ?")

with open( "studs.csv" , "a" , newline='' ) as file :
    # use of csv writer
    # writer = csv.writer(file)
    # writer.writerow([name,city])

    # use of dictionary writer
    writer = csv.DictWriter(file,fieldnames=["name","city"])
    writer.writerow({"name":name,"city":city})