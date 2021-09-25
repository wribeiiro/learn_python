from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('rosa', 2, 'ford', 20)

print('Cor:', caminhao_rosa.cor)
print('Rodas:', caminhao_rosa.rodas)
print('Marca:', caminhao_rosa.marca)
print('Tanque:', caminhao_rosa.tanque)

print('\n')

carro_azul = Carro('azul', 'xing ling', 30)

print('Cor:', carro_azul.cor)
print('Rodas:', carro_azul.rodas)
print('Marca:', carro_azul.marca)
print('Tanque:', carro_azul.tanque)
carro_azul.abastecer(465)
print('Tanque:', carro_azul.tanque)
