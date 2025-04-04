clients = [
 "  Ana López ", "Pedro Gómez", "maria martínez", "Pedro Gómez ", "",
 " Luis Rodríguez ", None, "ana lópez", "JUAN PÉREZ", "MARTA SUÁREZ",
 "luis rodríguez", "maría martínez ", " claudia torres", "CLAUDIA TORRES",
 "  ", "pedro gómez", "Juan Pérez", None, "Ricardo Fernández", "LAURA RAMOS",
 "carlos mendes", "RICARDO FERNÁNDEZ  ", " Laura ramos", "CARLOS MENDES",
 "alejandro gonzález", " ALEJANDRO GONZÁLEZ  ", "Patricia Vega",
 "patricia VEGA", "Andrés Ocampo", "  andrés ocampo", "Monica Herrera",
 "MONICA HERRERA  ", "gabriela ruíz", "Gabriela Ruíz", "sandra morales",
 "SANDRA MORALES", "miguel ángel", "Miguel Ángel ", " Damián Castillo",
 "Damián Castillo  ", None, "", "  "
 ]
newclients = [ aux.strip() for aux in clients if aux and aux.strip()]

newclients = [ aux.title() for aux in newclients ]

newclients = [ sorted(set(newclients)) ]

print(newclients)