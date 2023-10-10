'''with open("input.txt") as file, open("output.txt","w+") as new_file:
    number = file.readlines()
    for i in range(12):
        counter = 0
        if i == 1:
            summ=0
            for j in range(counter + 28):
                summ+=int(number[j][:-1])
            new_file.write(int(summ/28))
            counter +=28
        elif i == 11:
            for j in range(counter + 30):
                summ += int(number[j][:-1])
            summ += int(number[counter+31])
            new_file.write(int(summ/31))
        elif (i%2==0 and i!=1 and i!=11) or i==7:
            for j in range(counter + 31):
                summ += int(number[j][:-1])
            counter+=31
            new_file.write(int(summ / 31))
        else:
            for j in range(counter + 30):
                summ += int(number[j][:-1])
            counter+=30
            new_file.write(int(summ / 30))'''


with open("input.txt") as file, open("output.txt","w+") as new_file:
    number = file.readlines()
    counter = 0
    for i in range(12):
        if i == 1:
            summ = 0
            for j in range(counter,counter + 2):
                summ+=int(number[j][:-1])
            new_file.write(str(summ/2)+"\n")
            counter +=2
        elif i == 11:
            summ = 0
            for j in range(counter,counter + 3):
                summ += int(number[j][:-1])
            summ += int(number[counter+4])
            new_file.write(str(summ/4)+"\n")
        elif (i%2==0 and i!=1 and i!=11) or i==7:
            summ = 0
            for j in range(counter,counter + 4):
                summ += int(number[j][:-1])
            counter+=4
            new_file.write(str(summ / 4)+"\n")
        else:
            summ = 0
            for j in range(counter,counter + 3):
                summ += int(number[j][:-1])
            counter+=3
            new_file.write(str(summ / 3)+"\n")
