# Definicion de la tupla
tupla = (1, 2, 3, 4, 5)
lista = [10, 20, 30, 40]
# Dando a variables multiples
# uno, dos,tres, cuatro, cinco = tupla

# Haciendo sub tublas
# uno, *dos = tupla

# Comprimiendo tuplas y listas
resultado_comprimir = zip(tupla, lista)
# Casteo a una lista
resultado_comprimir = list(resultado_comprimir)
print(resultado_comprimir)


tupla_dos = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400)

# Sacamos el valor uno, dos y el ultimo
uno, dos, *_, ultimo = tupla_dos
print(uno, dos, ultimo)
