import numpy as np
import math
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# function to calculate the Taylor series approximation
def taylor_series_method(x, y0, h, order=3):
    y = y0
    derivatives = [y0**2 + x**2]  # first derivative
    for i in range(1, order):
        if i == 1:
            derivatives.append(2 * y * derivatives[i-1] + 2 * x)  # second derivative
        elif i == 2:
            derivatives.append(2 * (derivatives[i-1]**2 + y * derivatives[i-2]) + 2)  # third derivative
    y_approx = y + sum((derivatives[i] * (h**(i+1)) / math.factorial(i+1)) for i in range(order))
    return y_approx

# function to execute calculations and plot the graph
def execute_calculations():
    try:
        y0 = float(entry_y0.get())
        h1 = float(entry_h1.get())
        h2 = float(entry_h2.get())

        # calculate the approximations
        y_h1 = taylor_series_method(0, y0, h1)
        y_h2 = taylor_series_method(0, y0, h2)

        # display the results
        result_text.set(f"y(0.1) ≈ {y_h1:.4f}\ny(0.2) ≈ {y_h2:.4f}")

        # plot the approximations
        fig = Figure(figsize=(8, 5))
        ax = fig.add_subplot(111)
        ax.plot([0, h1, h2], [y0, y_h1, y_h2], 'bo-', label='Taylor Series Approximation')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title("Taylor Series Method")
        ax.legend()
        ax.grid(True)

        # display the plot in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=8, column=0, columnspan=6, padx=5, pady=5)

    except ValueError:
        result_text.set("Invalid input. Please enter valid numbers.")

# function to use predefined data
def use_predefined_data():
    entry_y0.delete(0, tk.END)
    entry_y0.insert(0, "1")
    entry_h1.delete(0, tk.END)
    entry_h1.insert(0, "0.1")
    entry_h2.delete(0, tk.END)
    entry_h2.insert(0, "0.2")
    execute_calculations()

# set up the GUI
root = tk.Tk()
root.title("Computational Mathematics - Task 7")

# input fields for initial condition and step sizes
tk.Label(root, text="y(0):").grid(row=0, column=0, padx=5, pady=5)
entry_y0 = tk.Entry(root)
entry_y0.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="h1 (step size for x=0.1):").grid(row=1, column=0, padx=5, pady=5)
entry_h1 = tk.Entry(root)
entry_h1.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="h2 (step size for x=0.2):").grid(row=1, column=2, padx=5, pady=5)
entry_h2 = tk.Entry(root)
entry_h2.grid(row=1, column=3, padx=5, pady=5)

# execute button
execute_button = tk.Button(root, text="Execute", command=execute_calculations)
execute_button.grid(row=2, column=0, columnspan=6, padx=5, pady=5)

# predefined data button
predefined_button = tk.Button(root, text="Use Predefined Data", command=use_predefined_data)
predefined_button.grid(row=3, column=0, columnspan=6, padx=5, pady=5)

# result display
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.grid(row=4, column=0, columnspan=6, padx=5, pady=5)

# run the GUI loop
root.mainloop()