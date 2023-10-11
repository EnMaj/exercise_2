with open("input.txt") as file, open("output.txt","w+"):
    mass = file.readlines()
    mass_number = []
    for i in range(len(mass)-1):
        if int(mass[i][:-1]) not in mass_number:
            mass_number.append(int(mass[i][:-1]))
    if int(mass[len(mass)-1]) not in mass_number:
        mass_number.append(int(mass[len(mass)-1]))
    mass_number.sort()
    print(mass_number)