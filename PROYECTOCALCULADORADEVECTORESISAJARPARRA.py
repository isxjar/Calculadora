import tkinter as tk
from tkinter import messagebox
import math

def distancia_entre_vectores(vector1, vector2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(vector1, vector2)))

def modulo(vector):
    return math.sqrt(sum([x ** 2 for x in vector]))

def suma_vectores(vector1, vector2):
    return [x + y for x, y in zip(vector1, vector2)]

def producto_punto(vector1, vector2):
    return sum(x * y for x, y in zip(vector1, vector2))

def angulo_entre_vectores(vector1, vector2):
    try:
        dot_product = producto_punto(vector1, vector2)
        mod_v1 = modulo(vector1)
        mod_v2 = modulo(vector2)
        cos_theta = dot_product / (mod_v1 * mod_v2)
        angle_rad = math.acos(cos_theta)
        angle_deg = math.degrees(angle_rad)
        return angle_deg
    except ZeroDivisionError:
        raise ValueError("El ángulo no está definido para vectores nulos.")

def producto_cruz(vector1, vector2):
    if len(vector1) == 3 and len(vector2) == 3:
        return [
            vector1[1] * vector2[2] - vector1[2] * vector2[1],
            vector1[2] * vector2[0] - vector1[0] * vector2[2],
            vector1[0] * vector2[1] - vector1[1] * vector2[0]
        ]
    else:
        raise ValueError("Los vectores deben ser de 3 dimensiones para el producto cruz.")

def calcular_distancia():
    try:
        vector1 = list(map(float, entry_vector1.get().split()))
        vector2 = list(map(float, entry_vector2.get().split()))
        result = distancia_entre_vectores(vector1, vector2)
        messagebox.showinfo("Resultado", f"La distancia entre los vectores es: {result}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")

def calcular_modulo():
    try:
        vector = list(map(float, entry_vector1.get().split()))
        result = modulo(vector)
        messagebox.showinfo("Resultado", f"El módulo del vector es: {result}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")

def calcular_suma():
    try:
        vector1 = list(map(float, entry_vector1.get().split()))
        vector2 = list(map(float, entry_vector2.get().split()))
        result = suma_vectores(vector1, vector2)
        messagebox.showinfo("Resultado", f"La suma de los vectores es: {result}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")

def calcular_producto_punto():
    try:
        vector1 = list(map(float, entry_vector1.get().split()))
        vector2 = list(map(float, entry_vector2.get().split()))
        result = producto_punto(vector1, vector2)
        messagebox.showinfo("Resultado", f"El producto punto de los vectores es: {result}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")

def calcular_angulo():
    try:
        vector1 = list(map(float, entry_vector1.get().split()))
        vector2 = list(map(float, entry_vector2.get().split()))
        result = angulo_entre_vectores(vector1, vector2)
        messagebox.showinfo("Resultado", f"El ángulo entre los vectores es: {result} grados")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def calcular_producto_cruz():
    try:
        vector1 = list(map(float, entry_vector1.get().split()))
        vector2 = list(map(float, entry_vector2.get().split()))
        result = producto_cruz(vector1, vector2)
        messagebox.showinfo("Resultado", f"El producto cruz de los vectores es: {result}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Vectores")

# Crear y colocar los widgets
label_instrucciones = tk.Label(root, text="Introduce los componentes de los vectores separados por espacio:")
label_instrucciones.pack(pady=10)

label_vector1 = tk.Label(root, text="Vector 1:")
label_vector1.pack()
entry_vector1 = tk.Entry(root, width=50)
entry_vector1.pack(pady=5)

label_vector2 = tk.Label(root, text="Vector 2:")
label_vector2.pack()
entry_vector2 = tk.Entry(root, width=50)
entry_vector2.pack(pady=5)

button_distancia = tk.Button(root, text="Calcular Distancia entre Vectores", command=calcular_distancia)
button_distancia.pack(pady=5)

button_modulo = tk.Button(root, text="Calcular Módulo de Vector 1", command=calcular_modulo)
button_modulo.pack(pady=5)

button_suma = tk.Button(root, text="Calcular Suma de Vectores", command=calcular_suma)
button_suma.pack(pady=5)

button_producto_punto = tk.Button(root, text="Calcular Producto Punto de Vectores", command=calcular_producto_punto)
button_producto_punto.pack(pady=5)

button_angulo = tk.Button(root, text="Calcular Ángulo entre Vectores", command=calcular_angulo)
button_angulo.pack(pady=5)

button_producto_cruz = tk.Button(root, text="Calcular Producto Cruz de Vectores", command=calcular_producto_cruz)
button_producto_cruz.pack(pady=5)

# Iniciar el bucle principal de la ventana
root.mainloop()
