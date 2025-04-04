rules = """Respeta a los demás. No se permiten insultos ni lenguaje ofensivo.
Evita el spam. No publiques enlaces sospechosos o repetitivos.
No compartas información personal.
Usa los canales adecuados para cada tema.
Sigue las instrucciones de los moderadores."""

aux = input("Ingrese palabra clave: ")
for line in rules.split("\n"):
    word = line.split()
    for act in word:
        if act.lower() == aux.lower():
            print(line)
            break