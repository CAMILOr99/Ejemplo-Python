pesos_COP = input("¿Cuantos pesos Colombianos tienes?: ")
pesos_COP = float(pesos_COP)
valor_dolar = 3981 #DOLAR EN PESOS COLOMBIANOS
dolares = pesos_COP / valor_dolar 
dolares = round(dolares, 4)
dolares = str(dolares)
print("Tienes $" + dolares + "dolares")
