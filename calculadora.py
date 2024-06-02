import tkinter as tk

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def raiz_cuadrada(x):
    if x < 0:
        return "Error: Número negativo"
    precision = 0.001
    g = x / 2.0
    while abs(g * g - x) > precision:
        g = (g + x / g) / 2
    return g

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def exponencial(x):
    precision = 0.001
    suma = 1  
    termino = 1
    n = 1
    while termino > precision:
        termino = (x ** n) / factorial(n)
        suma += termino
        n += 1
    return suma

class CalculadoraApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Científica")
        self.result_var = tk.StringVar()
        self.display = tk.Entry(master, textvariable=self.result_var)
        self.display.grid(row=0, column=0, columnspan=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()
