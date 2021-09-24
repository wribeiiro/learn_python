qtd_convidados = int(input("Quantidade de convidados: "))

if (qtd_convidados >= 5):
    print("O numero nao pode ser maior que 5")
    quit()

print("\n--------------------\n")

lista_convidados = []

for item in range(qtd_convidados):
    nome_convidado = input(f"Informe o nome do convidado número {item+1}: ")
    lista_convidados.append(nome_convidado)

print("\nNome dos convidados: \n--------------------\n")

for convidado in range(len(lista_convidados)):
    print(lista_convidados[convidado])
