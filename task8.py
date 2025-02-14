import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# function to compute the integral using simpson's 3/8 rule
def simpsons_38_rule(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("Number of subintervals must be a multiple of 3.")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    integral = (3 * h / 8) * (y[0] + y[-1] + 3 * np.sum(y[1:-1:3]) + 3 * np.sum(y[2:-1:3]) + 2 * np.sum(y[3:-3:3]))
    return integral, x, y

# function to compute the exact value of the integral
def exact_integral(a, b):
    return (b**4 / 4) - (a**4 / 4)

# function to execute calculations and display the results
def execute_calculations():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        n = int(entry_n.get())
        f_str = entry_f.get()
        f = eval(f"lambda x: {f_str}")

        # compute the integral using simpson's 3/8 rule
        integral_approx, x, y = simpsons_38_rule(f, a, b, n)

        # compute the exact value of the integral
        integral_exact = exact_integral(a, b)

        # compute the absolute error
        absolute_error = abs(integral_exact - integral_approx)

        # display the results
        result_text.set(f"Approximate Integral: {integral_approx:.6f}\nExact Integral: {integral_exact:.6f}\nAbsolute Error: {absolute_error:.6f}")

        # plot the function and the points
        fig = Figure(figsize=(8, 5))
        ax = fig.add_subplot(111)
        x_plot = np.linspace(a, b, 1000)
        y_plot = f(x_plot)
        ax.plot(x_plot, y_plot, label=f"f(x) = {f_str}")
        ax.plot(x, y, 'ro', label='Sample Points')
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title("Simpson's 3/8 Rule")
        ax.legend()
        ax.grid(True)

        # display the plot in the tkinter window
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    except ValueError as e:
        result_text.set(f"Error: {e}")

# function to use predefined data
def use_predefined_data():
    entry_a.delete(0, tk.END)
    entry_a.insert(0, "2")
    entry_b.delete(0, tk.END)
    entry_b.insert(0, "5")
    entry_n.delete(0, tk.END)
    entry_n.insert(0, "6")
    entry_f.delete(0, tk.END)
    entry_f.insert(0, "x**3")
    execute_calculations()

# set up the gui
root = tk.Tk()
root.title("Computational Mathematics - Task 8")

# input fields for integral limits, subintervals, and function
tk.Label(root, text="Lower limit (a):").grid(row=0, column=0, padx=5, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Upper limit (b):").grid(row=1, column=0, padx=5, pady=5)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Number of subintervals (n):").grid(row=2, column=0, padx=5, pady=5)
entry_n = tk.Entry(root)
entry_n.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Function (f):").grid(row=3, column=0, padx=5, pady=5)
entry_f = tk.Entry(root)
entry_f.grid(row=3, column=1, padx=5, pady=5)

# execute button
execute_button = tk.Button(root, text="Execute", command=execute_calculations)
execute_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# predefined data button
predefined_button = tk.Button(root, text="Use Predefined Data", command=use_predefined_data)
predefined_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# result display
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# run the gui loop
root.mainloop()