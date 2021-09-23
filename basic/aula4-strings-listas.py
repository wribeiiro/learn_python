frase = 'Oi, Tudo bem?'
lista_nomes = ['Joao', 'Maria', 'Pedro', 'Ola']

lista_nomes.append('Geralda')
print(lista_nomes)

lista_nomes.remove('Geralda')
print(lista_nomes)

lista_nomes.insert(1, 'Elemento1')
print(lista_nomes)

lista_nomes[1] = "Atualizado"
print(lista_nomes)

contador_lista = lista_nomes.count('Atualizado')
print(contador_lista)

frase_split = frase.split(',')
print(frase_split)