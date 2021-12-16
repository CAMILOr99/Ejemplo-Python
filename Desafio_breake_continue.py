def run():

    print('Bienvenido al contador de numeros') 
    
    LIMITE = int(input('Ingrese el numero limite a contar: '))
    numero = int(input('Ingrese el numero desde donde quiere que cuente: '))
    ROMPER = int(input('Ingrese el numero limite inferior donde quiere que se interrumpa la cuenta: '))

    while numero < LIMITE+1:
        print(numero)
        numero += 1
        if numero == ROMPER:
            break

if __name__ == '__main__':
    run()


