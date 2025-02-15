import os 
import shutil 

print(f"Directorio de trabajo actual: {os.getcwd()}")

# CREO LOS SUBDIRECTORIOS DESTINO 
os.makedirs("copia-ordenada", exist_ok=True)
os.makedirs("copia-ordenada/documentos", exist_ok=True)
os.makedirs("copia-ordenada/imagenes", exist_ok=True)
os.makedirs("copia-ordenada/videos", exist_ok=True)
os.makedirs("copia-ordenada/codigo", exist_ok=True)

# LISTO TODOS LOS ARCHIVOS DEL DIRECTORIO
archivos = os.listdir()

# ELIMINO EL PROPIO SCRIPT PARA QUE NO SE MUEVA A SI MISMO 
archivos = [archivo for archivo in archivos if archivo != os.path.basename(__file__)]

for archivo in archivos:
    if os.path.isfile(archivo):
        if archivo.endswith(".pdf"): 
            shutil.move(archivo, "copia-ordenada/documentos")
        elif archivo.endswith(".jpg") or archivo.endswith(".png"):
            shutil.move(archivo, "copia-ordenada/imagenes")
        elif archivo.endswith(".mp4"):
            shutil.move(archivo, "copia-ordenada/videos")
        elif archivo.endswith(".py"):
            shutil.move(archivo, "copia-ordenada/codigo")
        else:
            print(f"El archivo {archivo} no corresponde con ninguna extensión conocida")