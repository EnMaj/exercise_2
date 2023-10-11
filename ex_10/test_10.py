import os
os.mkdir('sample')
with open("input.txt") as file, open(r"sample\output.txt","w+") as new_file:
    mass_number = file.readlines()
    for i in range(len(mass_number)):
        if i%2==0:
            new_file.write(mass_number[i])


