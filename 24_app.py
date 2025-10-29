# Evaluación de Desempeño - Soluciones Tech

def registrar_empleados():
    empleados = []
    total = int(input("Ingrese la cantidad total de empleados a evaluar: "))

    for i in range(total):
        print(f"\nEmpleado {i + 1}:")
        codigo = input("Código único: ")
        nombre = input("Nombre completo: ")
        departamento = input("Departamento: ")

        # Ingreso y validación de puntajes
        puntajes = []
        competencias = ["Calidad de Trabajo", "Productividad", "Comunicación", "Puntualidad"]
        for comp in competencias:
            while True:
                try:
                    valor = float(input(f"Puntaje de {comp} (0-100): "))
                    if 0 <= valor <= 100:
                        puntajes.append(valor)
                        break
                    else:
                        print("⚠️ El puntaje debe estar entre 0 y 100.")
                except ValueError:
                    print("⚠️ Ingrese un número válido.")
        
        empleados.append({
            "codigo": codigo,
            "nombre": nombre,
            "departamento": departamento,
            "puntajes": tuple(puntajes)  # Guardar como tupla
        })
    
    return empleados


def calcular_puntaje(puntajes):
    pesos = (0.3, 0.3, 0.2, 0.2)
    return sum(p * w for p, w in zip(puntajes, pesos))


def clasificar(puntaje):
    if puntaje >= 90:
        return "Sobresaliente"
    elif puntaje >= 70:
        return "Cumple Expectativas"
    else:
        return "Necesita Mejora"


def generar_reporte(empleados):
    print("\n=== REPORTE FINAL ===")
    print(f"{'Código':<10} {'Nombre':<25} {'Puntaje':<10} {'Clasificación':<20}")
    print("-" * 70)

    # Estadísticas
    conteo = {"Sobresaliente": 0, "Cumple Expectativas": 0, "Necesita Mejora": 0}
    mayor = {"nombre": "", "puntaje": -1}
    menor = {"nombre": "", "puntaje": 999}

    for emp in empleados:
        puntaje = calcular_puntaje(emp["puntajes"])
        categoria = clasificar(puntaje)
        emp["puntaje"] = round(puntaje, 2)
        emp["categoria"] = categoria

        print(f"{emp['codigo']:<10} {emp['nombre']:<25} {emp['puntaje']:<10} {categoria:<20}")

        # Actualizar estadísticas
        conteo[categoria] += 1
        if puntaje > mayor["puntaje"]:
            mayor = {"nombre": emp["nombre"], "puntaje": puntaje}
        if puntaje < menor["puntaje"]:
            menor = {"nombre": emp["nombre"], "puntaje": puntaje}

    # Mostrar estadísticas finales
    print("\n=== ESTADÍSTICAS ===")
    for cat, total in conteo.items():
        print(f"Total {cat}: {total}")
    print(f"\nEmpleado con mayor puntaje: {mayor['nombre']} ({mayor['puntaje']:.2f})")
    print(f"Empleado con menor puntaje: {menor['nombre']} ({menor['puntaje']:.2f})")


def main():
    empleados = registrar_empleados()
    generar_reporte(empleados)


# Ejecución principal
if __name__ == "__main__":
    main()
