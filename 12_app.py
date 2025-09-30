comprobante = input("Digita el comprobante: ")
monto = input("Escribe el monto: ")

if comprobante == "factura":
    monto_igv = int(monto) * 0.18
    monto_a_pagar = int(monto) + monto_igv
    print(f"El monto total a pagar con factura es: {monto_a_pagar}")
elif comprobante == "boleta":
    print(f"El monto total a pagar con boleta es: {monto}")
else:
    print("Debe elegir un comprobante válido")