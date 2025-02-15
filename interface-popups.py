import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# 1º TIPO DE POPUP (MENSAJE DESPLEGABLE)
def popup_func1():
    messagebox.showinfo("Dark Style", "Dark style selected")


# 1º TIPO DE POPUP (versión redimensionable)
def popup_func1():
    popup = tk.Toplevel()
    popup.geometry("200x100")
    label = tk.Label(popup, text="Dark", font="Courier 20")
    label.pack(pady=20)


# 2º TIPO DE POPUP (INSERTAR DATOS)
def popup_func2():
    style = simpledialog.askstring("Input", "Introduce the style: ")
    if style: # Si se ha introducido algo
        messagebox.showinfo("Style", f"Style selected: {style}")

window = tk.Tk()

window.title("Styles")
window.geometry("800x800")

button = tk.Button(window, text="Dark Style", font="Courier 20", command=popup_func1)
button.pack(pady=100)

button2 = tk.Button(window, text="Select Style", font="Courier 20", command=popup_func2)
button2.pack(pady=35) 

tk.mainloop() 