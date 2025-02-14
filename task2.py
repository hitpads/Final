import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# define function and its derivative
def f(x):
    return x ** 2 - 4 * np.sin(x)

def df(x):
    return 2 * x - 4 * np.cos(x)

# false position method
def false_position(a, b, tol=1e-6, max_iter=100):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("The function must have different signs at the endpoints a and b.")

    for i in range(max_iter):
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        if abs(fc) < tol:
            return c, i + 1
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return c, max_iter

# newton-raphson method
def newton_raphson(x0, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        if abs(fx) < tol:
            return x0, i + 1
        x0 = x0 - fx / dfx
    return x0, max_iter

# function to execute calculations and plot graph
def execute_calculations():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        initial_guess = float(entry_initial_guess.get())

        # false position method
        root_fp, iter_fp = false_position(a, b)
        rel_error_fp = abs(f(root_fp))

        # newton-raphson method
        root_nr, iter_nr = newton_raphson(initial_guess)
        rel_error_nr = abs(f(root_nr))

        # generate x values for plotting
        x_values = np.linspace(a, b, 100)
        y_values = f(x_values)

        # plot the function
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(x_values, y_values, label=r'$f(x) = x^2 - 4\sin(x)$', color='blue')
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(root_fp, color='red', linestyle='--', label=f'False Position Root: {root_fp:.4f}')
        ax.axvline(root_nr, color='green', linestyle='--', label=f'Newton-Raphson Root: {root_nr:.4f}')
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title('Comparison of Root-Finding Methods')
        ax.legend()
        ax.grid(True)

        # display the plot in the tkinter window
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        # display results
        result_text.set(
            f"False Position Method:\nRoot: {root_fp:.6f}\nIterations: {iter_fp}\nRelative Error: {rel_error_fp:.6f}\n\n"
            f"Newton-Raphson Method:\nRoot: {root_nr:.6f}\nIterations: {iter_nr}\nRelative Error: {rel_error_nr:.6f}")
    except ValueError as e:
        result_text.set(str(e))
    except Exception as e:
        result_text.set("Invalid input. Please enter valid numbers.")

# function to use predefined data
def use_predefined_data():
    entry_a.delete(0, tk.END)
    entry_a.insert(0, "0")
    entry_b.delete(0, tk.END)
    entry_b.insert(0, "3")
    entry_initial_guess.delete(0, tk.END)
    entry_initial_guess.insert(0, "1.5")
    execute_calculations()

# set up the gui
root = tk.Tk()
root.title("Computational Mathematics - Task 2")

# input fields
tk.Label(root, text="a:").grid(row=0, column=0, padx=5, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="b:").grid(row=1, column=0, padx=5, pady=5)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Initial Guess:").grid(row=2, column=0, padx=5, pady=5)
entry_initial_guess = tk.Entry(root)
entry_initial_guess.grid(row=2, column=1, padx=5, pady=5)

# execute button
execute_button = tk.Button(root, text="Execute", command=execute_calculations)
execute_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# predefined data button
predefined_button = tk.Button(root, text="Use Predefined Data", command=use_predefined_data)
predefined_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# result display
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# run the gui loop
root.mainloop()
