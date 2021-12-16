#Menu de seleccion del pais segun los pesos
menu = """
Bienvenido al conversor de monedas 💲💰 

1 - pesos colombinos 
2 - pesos argentinos 
3 - pesos mexicanos

Elige una opcion: """

opcion=input(menu)

if opcion == '1':
    dolares = input("¿Cuantos dolares tienes?: ")
    dolares = float(dolares)
    valor_peso_COP = 3981 #DOLAR EN PESOS COLOMBIANOS
    peso_COP = valor_peso_COP*dolares 
    peso_COP = round(peso_COP, 4)
    peso_COP = str(peso_COP)
    print("Tienes $" + peso_COP + " " + "pesos colombianos")
elif opcion == '2':
    dolares = input("¿Cuantos dolares tienes?: ")
    dolares = float(dolares)
    valor_peso_arg = 100.68 #DOLAR EN PESOS ARGENTINOS
    valor_peso_arg= float(valor_peso_arg)
    peso_arg = valor_peso_arg*dolares 
    peso_arg = round(peso_arg, 4)
    peso_arg = str(peso_arg)
    print("Tienes $" + peso_arg + " " + "pesos argentinos")
elif opcion == '3':
    dolares = input("¿Cuantos dolares tienes?: ")
    dolares = float(dolares)
    valor_peso_mxc = 21.57 #DOLAR EN PESOS MEXICANOS
    valor_peso_mxc= float(valor_peso_mxc)
    peso_mxc = valor_peso_mxc*dolares 
    peso_mxc = round(peso_mxc, 4)
    peso_mxc = str(peso_mxc)
    print("Tienes $" + peso_mxc + " " + "pesos mexicanos")
else:
    print('Ingresa una opcion valida porfavor')
