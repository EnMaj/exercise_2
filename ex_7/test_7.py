try:
    with open("input.txt") as file, open("output.txt","w+") as new_file:
        number = file.readlines()
        n = str((int(number[0][:-1])/int(number[1][:-1]))+int(number[2]))
        new_file.write(n)
except ValueError:
    print("Невозможно строку преобразить в число")
except ZeroDivisionError:
    print("Невозможно делить на ноль")