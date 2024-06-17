import tkinter as tk
from tkinter import messagebox
import math

# Function definitions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def sqrt(x):
    if x < 0:
        return "Error: Square root of negative number!"
    return math.sqrt(x)

def exponentiate(x, y):
    return x ** y

# GUI implementation
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("400x500")

        self.entry = tk.Entry(self, width=16, font=('Arial', 24), bd=8, insertwidth=2, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sqrt', 'exp', 'C'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.click_event(x)
            tk.Button(self, text=button, padx=20, pady=20, bd=8, fg="black", font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def click_event(self, key):
        if key == '=':
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.entry.delete(0, tk.END)
        elif key == 'C':
            self.entry.delete(0, tk.END)
        elif key == 'sqrt':
            try:
                result = str(sqrt(float(self.entry.get())))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.entry.delete(0, tk.END)
        elif key == 'exp':
            try:
                base, exp = self.entry.get().split(',')
                result = str(exponentiate(float(base), float(exp)))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, key)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
