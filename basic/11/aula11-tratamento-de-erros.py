import time

def abre_arquivo():        
    try:
        open('teste.txt')
        return True
    except Exception as error:
        print("Deu ruim", error)
        return False

while not abre_arquivo():
    print('Tentando abrir oarquivo')
    time.sleep(5)

print('Consegui abrir o arquivo')