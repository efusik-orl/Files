with open("F1.txt", "w") as f1:
    while True:
        data = input("Введите данные (для окончания ввода введите пустую строку): ")
        if not data:
            break
        f1.write(data + "\n")

with open ("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
    for line in f1:
        if not any(char.isdigit() for char in line):
            f2.write(line)
