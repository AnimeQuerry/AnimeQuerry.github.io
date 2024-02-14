import json

def verify(json_data):
    verificated = []
    for item in json_data:
        default = {
            "id": item.get("id", 1),
            "title": item.get("title", ""),
            "alternativeTitles": item.get("alternativeTitles", []),
            "type": item.get("type", ""),
            "types": item.get("types", []),
            "tags": item.get("tags", []),
            "links": item.get("links", [])
        }
        verificated.append(default)
    return verificated

# Cargar el JSON desde el archivo
with open("./assets/database.json", "r") as file:
    data = json.load(file)

# Agregar la clave "categories" si no está presente
data = verify(data)

# Guardar el JSON modificado en un nuevo archivo
with open("./assets/database.json", "w") as file:
    json.dump(data, file, indent=4)

print("Se ha creado el archivo 'database.json' con el JSON modificado.")
