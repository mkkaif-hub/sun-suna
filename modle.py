import csv

with open("student.csv","w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "grade"])
    writer.writerow(["Alice", "20", "8th"])
    writer.writerow(["bob", "22", "9th"])

with open("student.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
