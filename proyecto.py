import hashlib
import urllib.request
import urllib.error
import random
import secrets
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

# Función para evaluar la fortaleza de una contraseña
def evaluar_fortaleza(password):
    puntuacion = 0
    criterios = []
    longitud = len(password)

    # Longitud
    if longitud >= 12:
        puntuacion += 30
        criterios.append("Longitud adecuada (>=12)")
    elif longitud >= 8:
        puntuacion += 15
        criterios.append("Longitud aceptable (8-11)")
    else:
        criterios.append("Longitud insuficiente (<8)")

    # Mayúsculas
    if any(c.isupper() for c in password):
        puntuacion += 20
        criterios.append("Contiene mayúsculas")
    else:
        criterios.append("No contiene mayúsculas")

    # Minúsculas
    if any(c.islower() for c in password):
        puntuacion += 20
        criterios.append("Contiene minúsculas")
    else:
        criterios.append("No contiene minúsculas")

    # Números
    if any(c.isdigit() for c in password):
        puntuacion += 15
        criterios.append("Contiene números")
    else:
        criterios.append("No contiene números")

    # Caracteres especiales
    if any(not c.isalnum() for c in password):
        puntuacion += 15
        criterios.append("Contiene caracteres especiales")
    else:
        criterios.append("No contiene caracteres especiales")

    if puntuacion > 100:
        puntuacion = 100

    mensaje = f"Puntaje: {puntuacion}%\n" + "\n".join(criterios)
    if puntuacion < 50:
        mensaje += "\n\n¡La contraseña es débil!"
    elif puntuacion < 80:
        mensaje += "\n\nLa contraseña es aceptable, pero podría mejorar."
    else:
        mensaje += "\n\n¡La contraseña es fuerte!"

    messagebox.showinfo("Resultado de fortaleza", mensaje)

# Función para generar contraseñas seguras
def generar_contrasena_segura(longitud=12):
    import string
    # Pedir longitud al usuario
    longitud_usuario = simpledialog.askinteger("Generar contraseña", "Longitud de la contraseña (mínimo 12):", minvalue=12, initialvalue=12)
    if not longitud_usuario:
        return
    longitud = max(12, longitud_usuario)
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasenas = []
    for _ in range(5):
        while True:
            contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
            # Validar que tenga al menos una mayúscula, una minúscula, un número y un símbolo
            if (any(c.isupper() for c in contrasena) and any(c.islower() for c in contrasena)
                and any(c.isdigit() for c in contrasena) and any(not c.isalnum() for c in contrasena)):
                contrasenas.append(contrasena)
                break
    mensaje = "Sugerencias de contraseñas seguras:\n\n" + "\n".join(contrasenas)
    messagebox.showinfo("Contraseñas seguras", mensaje)

# Interfaz gráfica con Tkinter
def mostrar_menu():
    def opcion_evaluar():
        password = simpledialog.askstring("Evaluar fortaleza", "Ingrese la contraseña a evaluar:")
        if password:
            evaluar_fortaleza(password)

    def opcion_generar():
        generar_contrasena_segura()

    root = tk.Tk()
    root.title("Analizador de Contraseñas")
    root.geometry("400x300")

    tk.Label(root, text="Analizador de Contraseñas", font=("Arial", 16)).pack(pady=20)
    tk.Button(root, text="Evaluar fortaleza de una contraseña", width=40, command=opcion_evaluar).pack(pady=5)
    tk.Button(root, text="Generar contraseñas seguras", width=40, command=opcion_generar).pack(pady=5)
    tk.Button(root, text="Salir", width=40, command=root.destroy).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    mostrar_menu()
