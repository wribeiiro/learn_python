import sys

argumentos = sys.argv

def soma(n1, n2):
    return float(n1) + float(n2)

def sub(n1, n2):
    return float(n1) - float(n2)

if argumentos[1] == 'soma':
    resp = soma(argumentos[2], argumentos[3])
elif argumentos[1] == 'sub':
    resp = sub(argumentos[2], argumentos[3])
else:
    print('Argumentos invalidos')
    quit()

print(resp)