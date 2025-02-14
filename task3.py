import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# jacobi method
def jacobi_method(A, b, x0, tol=1e-6, max_iter=100):
    n = len(b)
    x = x0.copy()
    iterations = []
    for k in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        iterations.append(x_new.copy())
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, k + 1, iterations
        x = x_new
    return x, max_iter, iterations

# function to execute calculations
def execute_calculations():
    try:
        A = np.array([
            [float(entry_a11.get()), float(entry_a12.get()), float(entry_a13.get())],
            [float(entry_a21.get()), float(entry_a22.get()), float(entry_a23.get())],
            [float(entry_a31.get()), float(entry_a32.get()), float(entry_a33.get())]
        ])
        b = np.array([float(entry_b1.get()), float(entry_b2.get()), float(entry_b3.get())])
        x0 = np.array([float(entry_x0.get()), float(entry_y0.get()), float(entry_z0.get())])

        # solve using jacobi method
        solution, iterations, iter_values = jacobi_method(A, b, x0)

        # display results
        result_text.set(f"Solution: {solution}\nIterations: {iterations}")

        # plot the iterations
        fig = Figure(figsize=(8, 5))
        ax = fig.add_subplot(111)
        iter_array = np.array(iter_values)
        for i in range(iter_array.shape[1]):
            ax.plot(range(1, iterations + 1), iter_array[:, i], label=f'x{i+1}')
        ax.set_xlabel('Iteration')
        ax.set_ylabel('Value')
        ax.set_title('Jacobi Method Iterations')
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
    entry_a11.delete(0, tk.END)
    entry_a11.insert(0, "3")
    entry_a12.delete(0, tk.END)
    entry_a12.insert(0, "1")
    entry_a13.delete(0, tk.END)
    entry_a13.insert(0, "-1")
    entry_a21.delete(0, tk.END)
    entry_a21.insert(0, "2")
    entry_a22.delete(0, tk.END)
    entry_a22.insert(0, "-8")
    entry_a23.delete(0, tk.END)
    entry_a23.insert(0, "1")
    entry_a31.delete(0, tk.END)
    entry_a31.insert(0, "-1")
    entry_a32.delete(0, tk.END)
    entry_a32.insert(0, "1")
    entry_a33.delete(0, tk.END)
    entry_a33.insert(0, "5")
    entry_b1.delete(0, tk.END)
    entry_b1.insert(0, "1")
    entry_b2.delete(0, tk.END)
    entry_b2.insert(0, "-2")
    entry_b3.delete(0, tk.END)
    entry_b3.insert(0, "3")
    entry_x0.delete(0, tk.END)
    entry_x0.insert(0, "0")
    entry_y0.delete(0, tk.END)
    entry_y0.insert(0, "0")
    entry_z0.delete(0, tk.END)
    entry_z0.insert(0, "0")
    execute_calculations()

# set up the gui
root = tk.Tk()
root.title("Computational Mathematics - Task 3")

# input fields for coefficients
tk.Label(root, text="a11:").grid(row=0, column=0, padx=5, pady=5)
entry_a11 = tk.Entry(root)
entry_a11.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="a12:").grid(row=0, column=2, padx=5, pady=5)
entry_a12 = tk.Entry(root)
entry_a12.grid(row=0, column=3, padx=5, pady=5)

tk.Label(root, text="a13:").grid(row=0, column=4, padx=5, pady=5)
entry_a13 = tk.Entry(root)
entry_a13.grid(row=0, column=5, padx=5, pady=5)

tk.Label(root, text="a21:").grid(row=1, column=0, padx=5, pady=5)
entry_a21 = tk.Entry(root)
entry_a21.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="a22:").grid(row=1, column=2, padx=5, pady=5)
entry_a22 = tk.Entry(root)
entry_a22.grid(row=1, column=3, padx=5, pady=5)

tk.Label(root, text="a23:").grid(row=1, column=4, padx=5, pady=5)
entry_a23 = tk.Entry(root)
entry_a23.grid(row=1, column=5, padx=5, pady=5)

tk.Label(root, text="a31:").grid(row=2, column=0, padx=5, pady=5)
entry_a31 = tk.Entry(root)
entry_a31.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="a32:").grid(row=2, column=2, padx=5, pady=5)
entry_a32 = tk.Entry(root)
entry_a32.grid(row=2, column=3, padx=5, pady=5)

tk.Label(root, text="a33:").grid(row=2, column=4, padx=5, pady=5)
entry_a33 = tk.Entry(root)
entry_a33.grid(row=2, column=5, padx=5, pady=5)

# input fields for constants
tk.Label(root, text="b1:").grid(row=3, column=0, padx=5, pady=5)
entry_b1 = tk.Entry(root)
entry_b1.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="b2:").grid(row=3, column=2, padx=5, pady=5)
entry_b2 = tk.Entry(root)
entry_b2.grid(row=3, column=3, padx=5, pady=5)

tk.Label(root, text="b3:").grid(row=3, column=4, padx=5, pady=5)
entry_b3 = tk.Entry(root)
entry_b3.grid(row=3, column=5, padx=5, pady=5)

# input fields for initial guess
tk.Label(root, text="x0:").grid(row=4, column=0, padx=5, pady=5)
entry_x0 = tk.Entry(root)
entry_x0.grid(row=4, column=1, padx=5, pady=5)

tk.Label(root, text="y0:").grid(row=4, column=2, padx=5, pady=5)
entry_y0 = tk.Entry(root)
entry_y0.grid(row=4, column=3, padx=5, pady=5)

tk.Label(root, text="z0:").grid(row=4, column=4, padx=5, pady=5)
entry_z0 = tk.Entry(root)
entry_z0.grid(row=4, column=5, padx=5, pady=5)

# execute button
execute_button = tk.Button(root, text="Execute", command=execute_calculations)
execute_button.grid(row=5, column=0, columnspan=6, padx=5, pady=5)

# predefined data button
predefined_button = tk.Button(root, text="Use Predefined Data", command=use_predefined_data)
predefined_button.grid(row=6, column=0, columnspan=6, padx=5, pady=5)

# result display
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.grid(row=7, column=0, columnspan=6, padx=5, pady=5)

# run the gui loop
root.mainloop()