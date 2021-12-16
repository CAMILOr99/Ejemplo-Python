def conversion_moneda(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos" + tipo_pesos + "tienes?: ")
    pesos= float(pesos)
    valor_dolar= float(valor_dolar)
    dolares = pesos / valor_dolar 
    dolares = round(dolares, 3)
    dolares = str(dolares)
    print("Tienes $" + dolares + " " + "dolares")    

#Menu de seleccion del pais segun los pesos
menu = """
Bienvenido al conversor de monedas 💲💰 

1 - pesos colombinos 
2 - pesos argentinos 
3 - pesos mexicanos

Elige una opcion: """

opcion=input(menu)

if opcion == '1':
    conversion_moneda("Colombianos", 3981)
elif opcion == '2':
    conversion_moneda("argentinos", 100.68)
elif opcion == '3':
    conversion_moneda("mexicanos", 21.57)
else:
    print('Ingresa una opcion valida porfavor')


