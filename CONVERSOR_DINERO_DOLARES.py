#Menu de seleccion del pais segun los pesos
menu = """
Bienvenido al conversor de monedas 💲💰 

1 - pesos colombinos 
2 - pesos argentinos 
3 - pesos mexicanos

Elige una opcion: """

opcion=input(menu)

if opcion == '1':
    pesos_COP = input("¿Cuantos pesos Colombianos tienes?: ")
    pesos_COP = float(pesos_COP)
    valor_dolar = 3981 #DOLAR EN PESOS COLOMBIANOS
    dolares = pesos_COP / valor_dolar 
    dolares = round(dolares, 4)
    dolares = str(dolares)
    print("Tienes $" + dolares + " " + "dolares")
elif opcion == '2':
    pesos_arg = input("¿Cuantos pesos Argentinos tienes?: ")
    pesos_arg = float(pesos_arg)
    valor_dolar = 100.68 #DOLAR EN PESOS ARGENTINOS
    valor_dolar= float(valor_dolar)
    dolares = pesos_arg / valor_dolar 
    dolares = round(dolares, 4)
    dolares = str(dolares)
    print("Tienes $" + dolares + " " + "dolares")
elif opcion == '3':
    pesos_mex = input("¿Cuantos pesos mexicanos tienes?: ")
    pesos_mex = float(pesos_mex)
    valor_dolar = 21.57 #DOLAR EN PESOS MEXICANOS
    valor_dolar= float(valor_dolar)
    dolares = pesos_mex / valor_dolar 
    dolares = round(dolares, 4)
    dolares = str(dolares)
    print("Tienes $" + dolares + " " + "dolares")

else:
    print('Ingresa una opcion valida porfavor')


