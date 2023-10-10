while True:
    fname = input()
    try:
        i=0
        with open(fname) as file:
            while True:
                n_line = input()
                try:
                    int_n_line = int(n_line)
                    for line in file:
                        i+=1
                        if i == int(int_n_line):
                            print(line)
                    break
                except ValueError:
                    print("Невозможно преобразовать строку в число")
        break
    except FileNotFoundError:
        print("Нет файла с таким именем")

