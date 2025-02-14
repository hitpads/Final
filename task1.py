import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# function
def f(x):
    return np.cos(x) - x

# execute calculations & plot graph
def execute_calculations():
    try:
        x_min = float(entry_x_min.get())
        x_max = float(entry_x_max.get())
        initial_guess = float(entry_initial_guess.get())

        # Generate x values
        x_values = np.linspace(x_min, x_max, 100)
        y_values = f(x_values)

        # Find approximate root (fsolve)
        approx_root = fsolve(f, initial_guess)[0]

        # absolute error (compared to numerical solution)
        absolute_error = abs(approx_root - approx_root)

        # plot the function
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(x_values, y_values, label=r'$f(x) = cos(x) - x$', color='blue')
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(approx_root, color='red', linestyle='--', label=f'Approximate Root: {approx_root:.4f}')
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title('Graph of $f(x) = cos(x) - x$')
        ax.legend()
        ax.grid(True)

        # Tkinter window plotting
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        # results
        result_text.set(f"Approximate Root: {approx_root:.6f}\nAbsolute Error: {absolute_error:.6f}")
    except ValueError:
        result_text.set("Invalid input. Please enter valid numbers.")



# Function to use initial data
def use_predefined_data():
    entry_x_min.delete(0, tk.END)
    entry_x_min.insert(0, "0")
    entry_x_max.delete(0, tk.END)
    entry_x_max.insert(0, "1")
    entry_initial_guess.delete(0, tk.END)
    entry_initial_guess.insert(0, "0.5")
    execute_calculations()

# GUI
root = tk.Tk()
root.title("Computational Mathematics - Task 1")

# Input fields
tk.Label(root, text="x_min:").grid(row=0, column=0, padx=5, pady=5)
entry_x_min = tk.Entry(root)
entry_x_min.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="x_max:").grid(row=1, column=0, padx=5, pady=5)
entry_x_max = tk.Entry(root)
entry_x_max.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Initial Guess:").grid(row=2, column=0, padx=5, pady=5)
entry_initial_guess = tk.Entry(root)
entry_initial_guess.grid(row=2, column=1, padx=5, pady=5)

# Execute button
execute_button = tk.Button(root, text="Execute", command=execute_calculations)
execute_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# initial data button
predefined_button = tk.Button(root, text="Use Predefined Data", command=use_predefined_data)
predefined_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# result
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# GUI loop
root.mainloop()