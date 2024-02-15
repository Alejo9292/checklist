import tkinter as tk
from tkinter import ttk
from A29 import PreVueloA29

def iniciar_pre_vuelo():
    numero_cola = "FAC3101"  # Ejemplo de número de cola, puedes cambiarlo si es necesario
    pre_vuelo_a29 = PreVueloA29(numero_cola, callback=lambda: None)  # Proporcionar un callback vacío

root = tk.Tk()
root.title("Seleccionar tipo de aeronave")

frame = ttk.Frame(root, padding="20")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label = ttk.Label(frame, text="Seleccionar tipo de aeronave:")
label.grid(column=0, row=0)

opciones = ["A29", "SA2-37"]
combo = ttk.Combobox(frame, values=opciones)
combo.grid(column=1, row=0)
combo.current(0)

boton_ejecutar = ttk.Button(frame, text="Ejecutar", command=iniciar_pre_vuelo)
boton_ejecutar.grid(column=0, row=1, columnspan=2, pady=10)

root.mainloop()
