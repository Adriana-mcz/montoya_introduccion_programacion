# Sistema de Registro y Análisis de Libros - Biblioteca Municipal

def ingresar_libros():
    """Registra los libros y devuelve una lista de diccionarios."""
    libros = []
    isbn_usados = set()  # para evitar códigos repetidos
    total = int(input("Ingrese la cantidad total de títulos a registrar: "))

    for i in range(total):
        print(f"\n Libro {i + 1}:")
        while True:
            isbn = input("Código ISBN (único y alfanumérico): ").strip()
            if isbn in isbn_usados:
                print("Ese ISBN ya está registrado. Ingrese otro.")
            elif isbn == "":
                print("El ISBN no puede estar vacío.")
            else:
                isbn_usados.add(isbn)
                break

        titulo = input("Título del libro: ").strip()
        genero = input("Género (Ficción, No-Ficción, Ciencia, Historia, etc.): ").strip()

        # Validación del precio
        while True:
            try:
                precio = float(input("Precio de reposición (en soles): "))
                if precio > 0:
                    break
                else:
                    print("El precio debe ser mayor a 0.")
            except ValueError:
                print("Ingrese un número válido.")

        # Validación del stock
        while True:
            try:
                stock = int(input("Cantidad de copias en stock: "))
                if stock >= 0:
                    break
                else:
                    print("El stock no puede ser negativo.")
            except ValueError:
                print("Ingrese un número entero válido.")

        # Tupla temporal con los tres primeros datos
        datos_basicos = (isbn, titulo, genero)

        # Crear diccionario del libro
        libro = {
            "isbn": datos_basicos[0],
            "titulo": datos_basicos[1],
            "genero": datos_basicos[2],
            "precio": precio,
            "stock": stock
        }

        libros.append(libro)

    return libros


def calcular_valor_total(libro):
    """Devuelve el valor total del libro (precio * stock)."""
    return libro["precio"] * libro["stock"]


def generar_reporte(libros):
    """Genera un reporte con estadísticas generales."""
    print("\n===== REPORTE FINAL DE LA COLECCIÓN =====")
    print(f"{'ISBN':<15} {'Título':<30} {'Género':<15} {'Precio':<10} {'Stock':<8} {'Valor Total':<12}")
    print("-" * 95)

    valor_total_coleccion = 0
    valores_por_genero = {}
    mayor_valor = {"titulo": "", "valor": -1}
    menor_valor = {"titulo": "", "valor": float("inf")}

    # Recorrer los libros
    for libro in libros:
        valor_libro = calcular_valor_total(libro)
        valor_total_coleccion += valor_libro

        # Acumular por género
        genero = libro["genero"]
        valores_por_genero[genero] = valores_por_genero.get(genero, 0) + valor_libro

        # Actualizar mayor y menor valor
        if valor_libro > mayor_valor["valor"]:
            mayor_valor = {"titulo": libro["titulo"], "valor": valor_libro}
        if valor_libro < menor_valor["valor"]:
            menor_valor = {"titulo": libro["titulo"], "valor": valor_libro}

        print(f"{libro['isbn']:<15} {libro['titulo']:<30} {libro['genero']:<15} "
              f"{libro['precio']:<10.2f} {libro['stock']:<8} {valor_libro:<12.2f}")

    # Género con mayor valor total
    genero_mayor_valor = max(valores_por_genero, key=valores_por_genero.get)

    # Mostrar estadísticas
    print("\n===== ESTADÍSTICAS =====")
    print(f"Valor total de la colección: S/. {valor_total_coleccion:.2f}")
    print(f"Género con mayor valor en inventario: {genero_mayor_valor} (S/. {valores_por_genero[genero_mayor_valor]:.2f})")
    print(f"Título con mayor valor: {mayor_valor['titulo']} (S/. {mayor_valor['valor']:.2f})")
    print(f"Título con menor valor: {menor_valor['titulo']} (S/. {menor_valor['valor']:.2f})")


def main():
    libros = ingresar_libros()
    generar_reporte(libros)


# Ejecución principal
if __name__ == "__main__":
    main()
