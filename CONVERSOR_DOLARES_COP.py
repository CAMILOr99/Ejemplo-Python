dolares = input("¿Cuantos dolares tienes?: ")
dolares = float(dolares)
valor_peso_COP = 3981 #DOLAR EN PESOS COLOMBIANOS
peso_COP = valor_peso_COP*dolares 
peso_COP = round(peso_COP, 4)
peso_COP = str(peso_COP)
print("Tienes $" + peso_COP + "pesos colombianos")