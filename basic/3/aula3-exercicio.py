nome = input("Nome: ")
idade = int(input("Idade: "))
peso = float(input("Peso: "))
altura = float(input("Altura: "))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print(nome, 'está apto para o exército!!!!')
else:
    print(nome, 'não está apto para o exército!')
