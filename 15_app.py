# Programa para calcular la tarifa de transporte según la edad del pasajero

# Definir las variables
edad = int(input("Ingrese la edad del pasajero: "))

# Determinar la tarifa según la edad
if edad < 12:
    tarifa = 3.00
    tipo_tarifa = "Tarifa infantil"
elif edad <= 59:
    tarifa = 5.00
    tipo_tarifa = "Tarifa regular"
else:
    tarifa = 2.00
    tipo_tarifa = "Tarifa especial"

# Salida: Visualización de resultados
print(f"{tipo_tarifa}: S/ {tarifa}")
