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
