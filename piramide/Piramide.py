#retirado do instagram @python.hub para fins de estudo

fila = 5

k = 0

for i in range(1, fila+1):

    for espaco in range(1, (fila-i)+1):
        print(end="")

    while k != (2*i-1):

        print("*", end = "")

        k += 1

    k = 0

    print()