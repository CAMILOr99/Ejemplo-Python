def es_primo(numero):
    if numero == 1:
        return False 
    else:
        contador = 0  
    for i in range(2,numero + 1):
        if i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


def run():
    numero = int(input('Escribe un numero: '))
    if es_primo(numero):
        print('El numero' + ' ' + str(numero) + ' ' + 'es primo')
    else:
        print('El numero' + ' ' + str(numero) + ' ' + 'no es primo')

if __name__ == '__main__':
    run()