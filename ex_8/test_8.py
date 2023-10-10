with open("input.txt") as file:
    number = file.readlines()
    for i in range(len(number)-1):
        if number[i][:-1] == "100":
            number.pop(i)
    if number[len(number) - 1] == "100":
        number.pop(len(number) - 1)
with open("input.txt","w") as file:
    for i in range(len(number)):
        file.write(number[i])

