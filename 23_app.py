# Listado de nombres
nombres = ["Juan", "Ana", "Jhon", "Luis", "Juan", "Carlos", "Ana"]

#Obteniendo número de repeticiones de elemento
print(nombres.count("Carlos"))
print(nombres.count("Juan"))

# Quitar elemntos de lista
nombres.pop(0)
print(nombres)

nombres.pop(3)
print(nombres)

# Ordenar elementos de lista
nombres.sort() # Ordena de manera ascendente
print(nombres)

nombres.sort(reverse=True) # Ordena de manera descendente
print(nombres)
