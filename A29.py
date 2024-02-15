import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import csv

class PreVueloA29:
    def __init__(self, numero_cola, callback):
        self.root_a29 = tk.Tk()

        self.pasos = [
            "Paso 1: Verificar fuselage",
            "Paso 2: Inspeccionar superficies de vuelo",
            "Paso 3: Revisar antenas",
            "Paso 4: Comprobar luces",
            "Paso 5: Inspeccionar silla de eyección",
            "Paso 6: Verificar sistema de armamento",
            "Paso 7: Inspeccionar frenos",
            "Paso 8: Revisar motor",
            "Paso 9: Calibrar instrumentos de navegación",
            "Paso 10: Verificar libro de vuelo"
        ]

        self.descripciones = [
            "Verificar el estado general del fuselaje.",
            "Inspeccionar las superficies de vuelo en busca de daños.",
            "Revisar el funcionamiento y estado de las antenas.",
            "Comprobar que todas las luces estén funcionando correctamente.",
            "Inspeccionar la silla de eyección y sus mecanismos de seguridad.",
            "Verificar el correcto funcionamiento del sistema de armamento.",
            "Inspeccionar el estado y funcionamiento de los frenos.",
            "Revisar el motor y sus sistemas asociados.",
            "Calibrar los instrumentos de navegación según los parámetros establecidos.",
            "Verificar que el libro de vuelo esté actualizado y completo."
        ]

        self.paso_actual = 0
        self.check_var = tk.BooleanVar()
        self.novedad_var = tk.BooleanVar()

        self.respuestas = []

        self.callback = callback  # Almacenar la función de retorno de llamada

        self.root_a29.title("Aplicación de Pre-vuelo A-29 - Paso {}".format(self.paso_actual + 1))
        self.root_a29.geometry("400x400")
        self.root_a29.configure(bg="gray")

        self.label_paso = tk.Label(self.root_a29, text=self.pasos[self.paso_actual], bg="gray", font=("Helvetica", 12))
        self.label_paso.pack(pady=10)

        self.label_anotacion = tk.Label(self.root_a29, text=self.descripciones[self.paso_actual], bg="gray")
        self.label_anotacion.pack(pady=5)

        self.check_button = tk.Checkbutton(self.root_a29, text="Paso Revisado", variable=self.check_var, command=self.actualizar_estado_continuar)
        self.check_button.pack(pady=10)

        self.novedad_button = tk.Checkbutton(self.root_a29, text="Novedad Observada", variable=self.novedad_var, command=self.actualizar_estado_continuar)
        self.novedad_button.pack(pady=10)

        self.cuadro_texto = tk.Entry(self.root_a29, width=40, state=tk.DISABLED)
        self.cuadro_texto.pack(pady=5)

        self.continuar_button = tk.Button(self.root_a29, text="Continuar", command=self.siguiente_paso_a29, state=tk.DISABLED)
        self.continuar_button.pack(pady=10)

    def actualizar_estado_continuar(self):
        if self.check_var.get() or self.novedad_var.get():
            self.continuar_button.config(state=tk.NORMAL)
        else:
            self.continuar_button.config(state=tk.DISABLED)

    def siguiente_paso_a29(self):
        respuesta = {
            "Paso": self.pasos[self.paso_actual],
            "Paso Revisado": self.check_var.get(),
            "Novedad Observada": self.novedad_var.get(),
            "Anotacion": self.cuadro_texto.get()
        }

        self.cuadro_texto.delete(0, tk.END)
        self.cuadro_texto.configure(state=tk.DISABLED)
        self.check_var.set(False)
        self.novedad_var.set(False)

        self.respuestas.append(respuesta)

        if self.paso_actual < len(self.pasos) - 1:
            self.paso_actual += 1
            self.label_paso.config(text=self.pasos[self.paso_actual])
            self.label_anotacion.config(text=self.descripciones[self.paso_actual])
            self.continuar_button.config(state=tk.DISABLED)  # Desactivar CONTINUAR al avanzar
        else:
            self.guardar_respuestas_en_csv()
            messagebox.showinfo("Mensaje", "Pre-vuelo A-29 completado. Respuestas guardadas en prevuelo_a29.csv")
            self.continuar_button.config(state=tk.DISABLED)

    def guardar_respuestas_en_csv(self):
        with open("prevuelo_a29.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(self.respuestas[0].keys())  # Escribir las cabeceras
            for respuesta in self.respuestas:
                writer.writerow(respuesta.values())

    def iniciar(self):
        self.root_a29.mainloop()
