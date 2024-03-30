#enconding: utf-8
import tkinter as tk
from tkinter import ttk

# Diccionarios de notas
notas_cifrado_bemoles = {
    0: "C",
    1: "Db",
    2: "D",
    3: "Eb",
    4: "E",
    5: "F",
    6: "Gb",
    7: "G",
    8: "Ab",
    9: "A",
    10: "Bb",
    11: "B",
}

notas_cifrado_sostenido = {
    0: "C",
    1: "C#",
    2: "D",
    3: "D#",
    4: "E",
    5: "F",
    6: "F#",
    7: "G",
    8: "G#",
    9: "A",
    10: "A#",
    11: "B",
}

#Recibe 2 argumentos los cuales son la nota y la escala a trabajar 
def obtener_valor_tonica(tonica, notas_cifrado):
    for valor, nota in notas_cifrado.items():
        if nota == tonica:
            return valor
    return None

# Funciones para generar acordes
def generar_acorde(tonica, tipo_acorde, sostenido):
    notas_cifrado = notas_cifrado_sostenido if sostenido else notas_cifrado_bemoles
    tonica_valor = obtener_valor_tonica(tonica, notas_cifrado)
    if tipo_acorde == "mayor":
        return generar_acorde_mayor(tonica_valor, notas_cifrado)
    elif tipo_acorde == "menor":
        return generar_acorde_menor(tonica_valor, notas_cifrado)
    elif tipo_acorde == "cinco":
        return generar_acorde_cinco(tonica_valor, notas_cifrado)
    elif tipo_acorde == "aum":
        return generar_acorde_aum(tonica_valor, notas_cifrado)
    elif tipo_acorde == "septima":
        return generar_acorde_septima(tonica_valor, notas_cifrado)
    elif tipo_acorde == "menorseptima":
        return generar_acorde_menorseptima(tonica_valor, notas_cifrado)
    elif tipo_acorde == "majseptima":
        return generar_acorde_majseptima(tonica_valor, notas_cifrado)

#Funcion para generar acorde mayor, recibe de argumentos el valor de la tónica en el diccionario 
#y el diccionario con el que se va a trabajar
def generar_acorde_mayor(tonica_valor, notas_cifrado):
    tercer_grado = notas_cifrado[(tonica_valor + 4) % 12]
    quinto_grado = notas_cifrado[(tonica_valor + 7) % 12]
    return [notas_cifrado[tonica_valor], tercer_grado, quinto_grado]



def generar_acorde_menor(tonica_valor, notas_cifrado):
    tercer_grado_bemol = notas_cifrado[(tonica_valor + 3) % 12]
    quinto_grado = notas_cifrado[(tonica_valor + 7) % 12]
    return [notas_cifrado[tonica_valor], tercer_grado_bemol, quinto_grado]

def generar_acorde_cinco(tonica_valor, notas_cifrado):
    quinto_grado = notas_cifrado[(tonica_valor + 7) % 12]
    return [notas_cifrado[tonica_valor], quinto_grado]

def generar_acorde_aum(tonica_valor, notas_cifrado):
    tercer_grado = notas_cifrado[(tonica_valor + 4) % 12]
    quinto_grado_aum = notas_cifrado[(tonica_valor + 8) % 12]
    return [notas_cifrado[tonica_valor], tercer_grado, quinto_grado_aum]

def generar_acorde_septima(tonica_valor, notas_cifrado):
    tercer_grado = notas_cifrado[(tonica_valor + 4) % 12]
    quinto_grado = notas_cifrado[(tonica_valor + 7) % 12]
    septima_bemol = notas_cifrado[(tonica_valor + 10) % 12]
    return [notas_cifrado[tonica_valor], tercer_grado, quinto_grado, septima_bemol]

def generar_acorde_menorseptima(tonica_valor, notas_cifrado):
    tercer_grado_bemol = notas_cifrado[(tonica_valor + 3) % 12]
    quinto_grado = notas_cifrado[(tonica_valor + 7) % 12]
    septima_bemol = notas_cifrado[(tonica_valor + 10) % 12]
    return [notas_cifrado[tonica_valor], tercer_grado_bemol, quinto_grado, septima_bemol]

def generar_acorde_majseptima(tonica_valor, notas_cifrado):
    tercer_grado = notas_cifrado[(tonica_valor + 4) % 12]
    quinto_grado = notas_cifrado[(tonica_valor + 7) % 12]
    septima = notas_cifrado[(tonica_valor + 11) % 12]
    return [notas_cifrado[tonica_valor], tercer_grado, quinto_grado, septima]




def generar_gui():
    #Creación de la ventana principal
    root = tk.Tk()
    root.title("Generador de Acordes")

    #Creación del marco principal
    main_frame = ttk.Frame(root, padding="20")
    main_frame.grid(row=0, column=0)

    # Función para generar el acorde seleccionado
    def generar_acorde_seleccionado():
        tonica = nota_combobox.get()
        tipo_acorde = acorde_combobox.get()
        sostenido = sostenido_var.get()
        acorde_generado = generar_acorde(tonica, tipo_acorde, sostenido)
        resultado_label.config(text=f"Acorde generado: {acorde_generado}")

    # Función para actualizar las notas cuando se cambia el checkbox
    def actualizar_notas():
        if sostenido_var.get():
            notas = list(notas_cifrado_sostenido.values())
        else:
            notas = list(notas_cifrado_bemoles.values())
            
        nota_combobox.config(values=notas)

    # Etiqueta y combobox para la selección de la nota
    nota_label = ttk.Label(main_frame, text="Selecciona la nota:")
    nota_label.grid(row=0, column=0, padx=5, pady=5)

    notas = list(notas_cifrado_bemoles.values())
    nota_combobox = ttk.Combobox(main_frame, values=notas)
    nota_combobox.grid(row=0, column=1, padx=5, pady=5)

    # Checkbox para elegir sostenidos
    sostenido_var = tk.BooleanVar()
    sostenido_checkbox = ttk.Checkbutton(main_frame, text="Usar sostenidos", variable=sostenido_var, command=actualizar_notas)
    sostenido_checkbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    # Etiqueta y combobox para la selección del tipo de acorde
    acorde_label = ttk.Label(main_frame, text="Selecciona el tipo de acorde:")
    acorde_label.grid(row=2, column=0, padx=5, pady=5)

    acordes = ["mayor", "menor", "cinco", "aum", "septima", "menorseptima", "majseptima"]
    acorde_combobox = ttk.Combobox(main_frame, values=acordes)
    acorde_combobox.grid(row=2, column=1, padx=5, pady=5)

    # Botón para generar el acorde seleccionado
    generar_button = ttk.Button(main_frame, text="Generar Acorde", command=generar_acorde_seleccionado)
    generar_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    # Etiqueta para mostrar el resultado
    resultado_label = ttk.Label(main_frame, text="")
    resultado_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    #Indica que la interfaz se va a repetir de forma indefinida
    root.mainloop()

generar_gui()