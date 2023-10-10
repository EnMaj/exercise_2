with open("input_1.txt") as file, open("output_1.txt", "w+") as file_new:
    for line in file:
        file_new.write(line.upper())