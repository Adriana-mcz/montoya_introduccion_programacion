# Variables

# Las variables son palabras específicas que utilizamos para asignar y almacenar valores específicos que podemos recuperar en cualquier momento.

# Variable nombre
nombre = "Jesús"
telefono = 997654111
name = "Alberto"

# Visualizando el contenido de las variables
print(nombre)
print(telefono)
print(name)

# Jugando con variables
age = 30
print(age)
print(f"Edad: {age}")

district = "San Luis"
print(district)
print(f"Nombre de Distrito: {district}")


#Es uncliente activo
is_active_client = True
print(is_active_client)
print(f"¿Está activo? {is_active_client}")


fecha_clase = date(2025, 9, 22) # (yyyy, mm, dd)
print(fecha_clase)
print(f"La fecha de hoy es: {fecha_clase}")

fecha_formateada = fecha_clase.strftime("%d/%m/%Y")
print(f"La fecha con formato es: {fecha_formateada}")