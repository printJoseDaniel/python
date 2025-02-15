import tkinter as tk 

window = tk.Tk()

# EL CÓDIGO DE PERSONALIZACIÓN TIENE QUE ESTAR ENTRE LA VENTANA Y EL MAINLOOP
window.title("Login")
window.geometry("500x500") 

# FUNCIÓN QUE SE EJECUTA CUANDO SE DA CLICK EN EL BOTÓN
def click():
    inputText = entry.get() # Obtiene el texto introducido en el entry
    label_introduced.config(text=f"'{inputText}' \nsuccessfully signed up") # Cambia el texto del label al hacer click en el botón


# ****************************************************************************************** 
# WIDGETS: 
 
# LABEL
label = tk.Label(window, text="Introduce your username:", font=("Courier", 20))
label.pack(pady=20) # pady añade x pixeles arriba y abajo 

# ENTRY (no almacena nada)
entry = tk.Entry(window, width=40)
entry.pack(pady=0)

# BUTTON
button = tk.Button(window, text="register", font="Courier 18", command=click) # click es una función que se ejecutará al hacer click en el botón
button.pack(pady=50)

# LABEL QUE SE EJECUTARÁ DESPUÉS PARA MOSTRAR LO QUE SE HA INTRODUCIDO EN EL ENTRY
label_introduced = tk.Label(window, text="", font=("Courier", 20))
label_introduced.pack(pady=10)


# ****************************************************************************************** 
# BUCLE INFINITO PARA MANTENER LA VENTANA ABIERTA 
window.mainloop()  