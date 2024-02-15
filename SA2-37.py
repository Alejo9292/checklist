import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import csv

def iniciar_prevuelo_a29(numero_cola):
    root_a29 = tk.Tk()

    pasos = [
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

    descripciones = [
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

    paso_actual = 0
    check_var = tk.BooleanVar()
    novedad_var = tk.BooleanVar()

    respuestas = []

    def habilitar_cuadro_texto(var, cuadro_texto):
        if var.get():
            cuadro_texto.configure(state=tk.NORMAL)
        else:
            cuadro_texto.delete(0, tk.END)
            cuadro_texto.configure(state=tk.DISABLED)

    def activar_continuar():
        if check_var.get():
            continuar_button.config(state=tk.NORMAL)
        else:
            continuar_button.config(state=tk.DISABLED)

    def siguiente_paso_a29():
        nonlocal paso_actual

        respuesta = {
            "Paso": pasos[paso_actual],
            "Paso Revisado": check_var.get(),
            "Novedad Observada": novedad_var.get(),
            "Anotacion": cuadro_texto.get()
        }

        cuadro_texto.delete(0, tk.END)
        cuadro_texto.configure(state=tk.DISABLED)
        check_var.set(False)
        novedad_var.set(False)

        respuestas.append(respuesta)

        if paso_actual < len(pasos) - 1:
            paso_actual += 1
            label_paso.config(text=pasos[paso_actual])
            label_anotacion.config(text=descripciones[paso_actual])
            continuar_button.config(state=tk.DISABLED)  # Desactivar CONTINUAR al avanzar
        else:
            guardar_respuestas_en_csv(respuestas)
            messagebox.showinfo("Mensaje", "Pre-vuelo A-29 completado. Respuestas guardadas en prevuelo_a29.csv")
            continuar_button.config(state=tk.DISABLED)

    def guardar_respuestas_en_csv(respuestas):
        with open("prevuelo_a29.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(respuestas[0].keys())  # Escribir las cabeceras
            for respuesta in respuestas:
                writer.writerow(respuesta.values())

    root_a29.title("Aplicación de Pre-vuelo A-29 - Paso {}".format(paso_actual + 1))
    root_a29.geometry("400x400")
    root_a29.configure(bg="gray")

    label_paso = tk.Label(root_a29, text=pasos[paso_actual], bg="gray", font=("Helvetica", 12))
    label_paso.pack(pady=10)

    label_anotacion = tk.Label(root_a29, text=descripciones[paso_actual], bg="gray")
    label_anotacion.pack(pady=5)

    check_button = tk.Checkbutton(root_a29, text="Paso Revisado", variable=check_var, command=activar_continuar)
    check_button.pack(pady=10)

    novedad_button = tk.Checkbutton(root_a29, text="Novedad Observada", variable=novedad_var, command=lambda: habilitar_cuadro_texto(novedad_var, cuadro_texto))
    novedad_button.pack(pady=10)

    cuadro_texto = tk.Entry(root_a29, width=40, state=tk.DISABLED)
    cuadro_texto.pack(pady=5)

    continuar_button = tk.Button(root_a29, text="Continuar", command=siguiente_paso_a29, state=tk.DISABLED)
    continuar_button.pack(pady=10)

    root_a29.mainloop()

if __name__ == "__main__":
    iniciar_prevuelo_a29("FAC3101")  # Puedes cambiar el número de cola según sea necesario
