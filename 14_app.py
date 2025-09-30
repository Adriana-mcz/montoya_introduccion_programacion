# Programa para convertir soles (PEN) a dólares (USD)

# Inicio: Definir o crear las variables
monto_en_soles = float(input("Ingrese el monto en soles (PEN): "))
tasa_de_cambio = float(input("Ingrese la tasa de cambio actual (1 USD = ? PEN): "))

# Proceso: Realizar las operaciones de cálculo
equivalente_dolares = monto_en_soles / tasa_de_cambio

# Salida: Visualización de resultados
print(f"--- Conversión en Global Change ---")
print(f"Monto en soles: S/ {monto_en_soles}")
print(f"Tasa de cambio: 1 USD = S/ {tasa_de_cambio}")
print(f"Equivalente en dólares: $ {equivalente_dolares}")
