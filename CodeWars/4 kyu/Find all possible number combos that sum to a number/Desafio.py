number = int(input("Digite o numero que quer saber: "))

def combos(n):
    resultados = []

    def buscar(atual, soma, inicio):
        if soma == n:
            resultados.append(atual[:])
            return

        if soma > n:
            return


        for i in range(inicio, n + 1):
            atual.append(i)
            buscar(atual, soma + i, i)
            atual.pop()
    buscar([], 0, 1)
    return resultados

print(combos(number))
