descriptions = [
"Streaming de música en vivo con covers y composiciones",
"Charla interactiva con la audiencia sobre series y películas",
"Jugamos a juegos retro y charlamos sobre su historia",
"Exploramos la mejor música de los 80s y 90s",
"Programa de entretenimiento con noticias y curiosidades del mundo gamer",
"Sesión de charla con invitados especiales del mundo del streaming",
"Música en directo con improvisaciones y peticiones del chat",
"Un espacio para charlar relajada sobre tecnología y cultura digital",
"Exploramos el impacto de la música en los videojuegos clásicos"
]

mus = 0
cha = 0
ent = 0

for line in descriptions:
    word = line.split()
    for act in word:
     if (act.lower() == "música"):
          mus = mus + 1
          break
     if (act.lower() == "charla"):
          cha = cha + 1
          break
     if (act.lower() == "entretenimiento"):
          ent = ent + 1
          break
print(f"Menciones de 'música': {mus}")
print(f"Menciones de 'charla': {cha}")
print(f"Menciones de 'entretenimiento': {ent}")