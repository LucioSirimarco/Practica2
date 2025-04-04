titles = [
"Speedrun de Super Mario en tiempo récord",
"Charla sobre desarrollo de videojuegos",
"Jugando al nuevo FPS del momento con amigos",
"Música en vivo: improvisaciones al piano"
]

max = 0

for text in titles:
    words = text.split()
    if len(words) > max:
        max = len(words)
        act = words
print(act)