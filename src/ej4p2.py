import os
while True:
    numero = False
    may = False
    simbolos = True
    name = input("Ingrese el nombre de usuario: ")
    for char in name:
        if char.isdigit():
            numero = True
        if char.isalpha():
            may = True
        if not(char.isalnum()):
            simbolos = False
    if (len(name)>= 5) and (numero) and (may) and (simbolos):
        print("Usuario aceptado!")
        break
    else: 
        print("Usuario incorrecto")