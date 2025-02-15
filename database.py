import tkinter as tk

window = tk.Tk()

# EL CÓDIGO DE PERSONALIZACIÓN TIENE QUE ESTAR ENTRE LA VENTANA Y EL MAINLOOP
window.title("Mi first interface")
window.geometry("500x500") 

def click():
    label.config
    label.config(text="Button clicked") # Cambia el texto del label al hacer click en el botón

# ****************************************************************************************** 
# WIDGETS: 
 
# LABEL
label = tk.Label(window, text="My label widget", font=("Courier", 20))
label.pack(pady=200)

# BUTTON
button = tk.Button(window, text="click me", font="Courier 15", command=click) # click es una función que se ejecutará al hacer click en el botón
button.pack(pady=15)

# BUCLE INFINITO PARA MANTENER LA VENTANA ABIERTA 
window.mainloop()  