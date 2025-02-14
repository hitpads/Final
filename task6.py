import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# function to calculate the first derivative using newton's forward difference formula
def calculate_derivative(x, y):
    h = x[1] - x[0]
    delta_y = np.diff(y)
    dy_dx = (delta_y[0] + delta_y[1]) / (2 * h)
    return dy_dx

# function to execute calculations and plot the graph
def execute_calculations():
    try:
        x = np.array([float(entry_x0.get()), float(entry_x1.get()), float(entry_x2.get())])
        y = np.array([float(entry_y0.get()), float(entry_y1.get()), float(entry_y2.get())])

        # calculate the derivative
        dy_dx = calculate_derivative(x, y)

        # display the result
        result_text.set(f"Estimated dy/dx at x=1: {dy_dx:.2f}")

        # plot the data points and the estimated derivative
        fig = Figure(figsize=(8, 5))
        ax = fig.add_subplot(111)
        ax.plot(x, y, 'bo-', label='Data points')
        ax.axhline(dy_dx, color='r', linestyle='--', label=f'Estimated dy/dx at x=1: {dy_dx:.2f}')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title("First Derivative Using Newton's Forward Difference Formula")
        ax.legend()
        ax.grid(True)

        # display the plot in the tkinter window
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=8, column=0, columnspan=6, padx=5, pady=5)

    except ValueError:
        result_text.set("Invalid input. Please enter valid numbers.")

# function to use predefined data
def use_predefined_data():
    entry_x0.delete(0, tk.END)
    entry_x0.insert(0, "0")
    entry_x1.delete(0, tk.END)
    entry_x1.insert(0, "1")
    entry_x2.delete(0, tk.END)
    entry_x2.insert(0, "2")
    entry_y0.delete(0, tk.END)
    entry_y0.insert(0, "1")
    entry_y1.delete(0, tk.END)
    entry_y1.insert(0, "3")
    entry_y2.delete(0, tk.END)
    entry_y2.insert(0, "7")
    execute_calculations()

# set up the gui
root = tk.Tk()
root.title("Computational Mathematics - Task 6")

# input fields for data points
tk.Label(root, text="x0:").grid(row=0, column=0, padx=5, pady=5)
entry_x0 = tk.Entry(root)
entry_x0.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="x1:").grid(row=0, column=2, padx=5, pady=5)
entry_x1 = tk.Entry(root)
entry_x1.grid(row=0, column=3, padx=5, pady=5)

tk.Label(root, text="x2:").grid(row=0, column=4, padx=5, pady=5)
entry_x2 = tk.Entry(root)
entry_x2.grid(row=0, column=5, padx=5, pady=5)

tk.Label(root, text="y0:").grid(row=1, column=0, padx=5, pady=5)
entry_y0 = tk.Entry(root)
entry_y0.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="y1:").grid(row=1, column=2, padx=5, pady=5)
entry_y1 = tk.Entry(root)
entry_y1.grid(row=1, column=3, padx=5, pady=5)

tk.Label(root, text="y2:").grid(row=1, column=4, padx=5, pady=5)
entry_y2 = tk.Entry(root)
entry_y2.grid(row=1, column=5, padx=5, pady=5)

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

# run the gui loop
root.mainloop()