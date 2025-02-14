import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# function to perform linear curve fitting using least squares
def linear_curve_fitting(x, y):
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    return m, c

# function to execute calculations and plot the graph
def execute_calculations():
    try:
        x = np.array([float(entry_x1.get()), float(entry_x2.get()), float(entry_x3.get()), float(entry_x4.get()), float(entry_x5.get())])
        y = np.array([float(entry_y1.get()), float(entry_y2.get()), float(entry_y3.get()), float(entry_y4.get()), float(entry_y5.get())])

        # perform linear curve fitting
        m, c = linear_curve_fitting(x, y)

        # display the result
        result_text.set(f"Fitted line: y = {m:.2f}x + {c:.2f}")

        # plot the data points and the fitted line
        fig = Figure(figsize=(8, 5))
        ax = fig.add_subplot(111)
        ax.plot(x, y, 'bo', label='Data points')
        ax.plot(x, m*x + c, 'r-', label=f'Fitted line: y = {m:.2f}x + {c:.2f}')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title("Linear Curve Fitting using Least Squares")
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
    entry_x1.delete(0, tk.END)
    entry_x1.insert(0, "1")
    entry_x2.delete(0, tk.END)
    entry_x2.insert(0, "2")
    entry_x3.delete(0, tk.END)
    entry_x3.insert(0, "3")
    entry_x4.delete(0, tk.END)
    entry_x4.insert(0, "4")
    entry_x5.delete(0, tk.END)
    entry_x5.insert(0, "5")
    entry_y1.delete(0, tk.END)
    entry_y1.insert(0, "5")
    entry_y2.delete(0, tk.END)
    entry_y2.insert(0, "8")
    entry_y3.delete(0, tk.END)
    entry_y3.insert(0, "12")
    entry_y4.delete(0, tk.END)
    entry_y4.insert(0, "15")
    entry_y5.delete(0, tk.END)
    entry_y5.insert(0, "20")
    execute_calculations()

# set up the gui
root = tk.Tk()
root.title("Computational Mathematics - Task 5")

# input fields for data points
tk.Label(root, text="x1:").grid(row=0, column=0, padx=5, pady=5)
entry_x1 = tk.Entry(root)
entry_x1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="x2:").grid(row=0, column=2, padx=5, pady=5)
entry_x2 = tk.Entry(root)
entry_x2.grid(row=0, column=3, padx=5, pady=5)

tk.Label(root, text="x3:").grid(row=0, column=4, padx=5, pady=5)
entry_x3 = tk.Entry(root)
entry_x3.grid(row=0, column=5, padx=5, pady=5)

tk.Label(root, text="x4:").grid(row=1, column=0, padx=5, pady=5)
entry_x4 = tk.Entry(root)
entry_x4.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="x5:").grid(row=1, column=2, padx=5, pady=5)
entry_x5 = tk.Entry(root)
entry_x5.grid(row=1, column=3, padx=5, pady=5)

tk.Label(root, text="y1:").grid(row=2, column=0, padx=5, pady=5)
entry_y1 = tk.Entry(root)
entry_y1.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="y2:").grid(row=2, column=2, padx=5, pady=5)
entry_y2 = tk.Entry(root)
entry_y2.grid(row=2, column=3, padx=5, pady=5)

tk.Label(root, text="y3:").grid(row=2, column=4, padx=5, pady=5)
entry_y3 = tk.Entry(root)
entry_y3.grid(row=2, column=5, padx=5, pady=5)

tk.Label(root, text="y4:").grid(row=3, column=0, padx=5, pady=5)
entry_y4 = tk.Entry(root)
entry_y4.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="y5:").grid(row=3, column=2, padx=5, pady=5)
entry_y5 = tk.Entry(root)
entry_y5.grid(row=3, column=3, padx=5, pady=5)

# execute button
execute_button = tk.Button(root, text="Execute", command=execute_calculations)
execute_button.grid(row=4, column=0, columnspan=6, padx=5, pady=5)

# predefined data button
predefined_button = tk.Button(root, text="Use Predefined Data", command=use_predefined_data)
predefined_button.grid(row=5, column=0, columnspan=6, padx=5, pady=5)

# result display
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.grid(row=6, column=0, columnspan=6, padx=5, pady=5)

# run the gui loop
root.mainloop()