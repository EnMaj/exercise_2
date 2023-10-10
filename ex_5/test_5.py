while True:
    fname = input()
    try:
        i=0
        with open(fname) as file:
            n_line = int(input())
            for line in file:
                i+=1
                if i == n_line:
                    print(line)
        break
    except FileNotFoundError:
        print("Нет файла с таким именем")
    except ValueError:
        print("Невозможно преобразовать строку в число")



