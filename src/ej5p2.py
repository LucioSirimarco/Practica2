
velocidad = int (input("Ingrese la velocidad en ms: "))
if (velocidad < 200):
    print("Categoria: rapido")
elif ( 200 < velocidad < 500 ):
    print("Categoria: normal")
else:
    print("Categoria: lento")
