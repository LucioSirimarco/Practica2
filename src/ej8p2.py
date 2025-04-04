
primera = input("Ingrese la primera palabra: ")
segunda = input("Ingrese la segunda palabra: ")

if sorted(primera) == sorted(segunda):
    print("Son anagramas")
else:
    print("No son anagramas")

