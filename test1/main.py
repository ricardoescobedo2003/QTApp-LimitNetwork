import json

# Función para obtener los datos del cliente desde el teclado
def obtener_datos_cliente():
    nombre = input("Introduce el nombre del cliente: ")
    edad = int(input("Introduce la edad del cliente: "))
    correo = input("Introduce el correo del cliente: ")
    calle = input("Introduce la calle de la dirección del cliente: ")
    ciudad = input("Introduce la ciudad de la dirección del cliente: ")
    codigo_postal = input("Introduce el código postal de la dirección del cliente: ")
    telefono = input("Introduce el teléfono del cliente: ")
    
    cliente = {
        "nombre": nombre,
        "edad": edad,
        "correo": correo,
        "direccion": {
            "calle": calle,
            "ciudad": ciudad,
            "codigo_postal": codigo_postal
        },
        "telefono": telefono
    }
    
    return cliente

# Obtener los datos del cliente desde el teclado
cliente = obtener_datos_cliente()

# Guardar los datos del cliente en un archivo JSON
with open('cliente.json', 'w') as archivo_json:
    json.dump(cliente, archivo_json, indent=4)

# Leer los datos desde el archivo JSON
with open('cliente.json', 'r') as archivo_json:
    datos_cliente = json.load(archivo_json)
    print("Datos del cliente leídos desde el archivo JSON:")
    print(datos_cliente)
