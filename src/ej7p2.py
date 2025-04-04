import string
import random
name = input("Ingrese el nombre: ")
while len(name) > 15:
    name = input("Ingrese un nombre con menos de 15 letras")
fecha = input("Ingrese la fecha actual:")
aleatorio = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
codigo =  name + fecha + aleatorio
print(f"El codigo es: {codigo}")