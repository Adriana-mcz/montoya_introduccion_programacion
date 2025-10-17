# Programa para calcular el precio final de un producto con descuento

def calcularMonto(precio, descuento):
    montoDescuento = precio * (descuento/100)
    montoPago = precio - montoDescuento
    return montoPago

# Utilizando la función
