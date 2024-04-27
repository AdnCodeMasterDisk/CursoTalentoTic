altura = int(input(" "))

for i in range(1, altura - 1):
    for j in range(i * 2 - 1, 0, -2):
        print(j, end=" ")
    print()
