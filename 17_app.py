# Ejercico 02 - Funciones

# Convertir de soles a dólares
def convertirMoneda (montoSoles,tipoCambio):
    montoDolares = montoSoles / tipoCambio
    return montoDolares

# Utilizando la función 
compraDolares = convertirMoneda (2000, 3.48)
print(f"El monto en dólares es: ${compraDolares:.2f} dólares")