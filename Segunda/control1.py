mes = int(input("Ingresa un mes (1-12): "))

if (mes >=9 or mes <=11):
    print("OTONO")
elif (mes == 1 or mes == 2 or mes == 12):
    print("INVIERNO")
elif (mes >=3 or mes <=5):
    print("PRIMAVERA")
elif (mes >=6 or mes <=8):
    print("VERANO")
else: 
    print("No válida")