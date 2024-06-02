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

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3), ('sqrt', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3), ('exp', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3), ('=', 3, 4),
            ('0', 4, 0), ('C', 4, 1), ('.', 4, 2), ('/', 4, 3)
        ]
        for (text, row, column) in buttons:
            button = tk.Button(master, text=text, command=lambda t=text: self.click(t))
            button.grid(row=row, column=column, sticky="nsew")

        self.master.grid_rowconfigure(1, weight=1)
        for i in range(5):
            self.master.grid_columnconfigure(i, weight=1)

    def click(self, key):
        if key == 'C':
            self.result_var.set("")
        elif key == '=':
            try:
                result = eval(self.result_var.get(), {"__builtins__": None}, {
                    'suma': suma, 'resta': resta, 'multiplicacion': multiplicacion, 
                    'division': division, 'raiz_cuadrada': raiz_cuadrada, 'exponencial': exponencial
                })
                self.result_var.set(str(result))
            except:
                self.result_var.set("Error")
        elif key in ('sqrt', 'exp'):
            try:
                current_val = float(self.display.get())
                if key == 'sqrt':
                    result = raiz_cuadrada(current_val)
                else:
                    result = exponencial(current_val)
                self.result_var.set(str(result))
            except ValueError:
                self.result_var.set("Error")
        else:
            self.result_var.set(self.result_var.get() + key)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()
