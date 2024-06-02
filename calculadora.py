import tkinter as tk

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
