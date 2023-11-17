import codecs

with codecs.open("Employees.txt", "r", "utf-8") as f:
    lines = f.readlines()
    employees = []
    for line in lines:
        name, salary = line.split()
        employees.append((name, int(salary)))

print('Сотрудники с окладом более 2000: ')
for employee in employees:
    if employee[1] > 2000:
        print(employee[0])
