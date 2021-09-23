def maior_numero(colecao):
    maior_numero = 0

    for numero in colecao:
        if numero > maior_numero:
            maior_numero = numero

    return maior_numero

teste_maior_numero = maior_numero([16, 32, 88, 99, 5, 23, 543, 2344, 32, 124, 47, 975])

print(teste_maior_numero)