#Palindromo para ver palabras que se leen igual al contrario
def palindromo(palabra):
    palabra = palabra.replace(' ','')#remplazo espacios por nada
    palabra = palabra.lower()#colocar la palbra en minusculas
    palabra_invertida = palabra[::-1]#tomo la palabra invertida
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra o una frase porfavor: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')

if __name__ == '__main__':
    run()