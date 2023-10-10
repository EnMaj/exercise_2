fname = input()
try:
    n_line = int(input())
    i=0
    with open(fname) as file:
        for line in file:
            i+=1
            if i == n_line:
                print(line)
except FileNotFoundError:
    print("Нет файла с таким именем")
except ValueError:
    print("Невозможно преобразовать строку в число")

