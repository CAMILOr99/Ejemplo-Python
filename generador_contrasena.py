import random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D' , 'F' , 'G', 'H', 'I', 'J', 'K',
     'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
     'Y', 'Z']

    minusculas = ['a', 'b', 'c', 'd' , 'f' , 'g', 'h', 'i', 'j', 'k',
     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
     'y', 'z']

    simbolos = ['!', '#', '$', '&', '/', '(' , ')']

    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(15):
        carcter_random = random.choice(caracteres)
        contrasena.append(carcter_random)

    contrasena = "".join(contrasena) #generar un string de una lista
    return contrasena

    
def run():
    contrasena = generar_contrasena()
    print('Tu nueva contrasena es: ' + contrasena)

if __name__ == '__main__':
    run()