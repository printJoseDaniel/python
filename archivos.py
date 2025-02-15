# LEER DE UN FICHERO
with open('datos.txt', 'r') as archivo:
    contenido=archivo.read()
    print(contenido)

# ESCRIBIR EN UN FICHERO --> WRITE
with open('datos.txt', 'w') as archivo:
    archivo.write('Este nuevo contenido del archivo') # Sobreescritura

# ESCRIBIR EN UN FICHERO --> APPEND
with open('datos.txt', 'a') as archivo:
    archivo.write('\nEsto se añade al contenido del archivo') # Append

# LEER DE UN FICHERO LINEA POR LINEA
with open('datos.txt', 'r') as archivo:
    print('\nLeyendo el archivo por lineas:')
    for linea in archivo:
        print(linea, end='')

