import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# function to compute inverse using iterative method
def iterative_matrix_inverse(A, tol=1e-6, max_iter=100):
    n = A.shape[0]
    I = np.eye(n)
    trace_A = np.trace(A)
    alpha = 1 / trace_A  # initial approximation
    X = alpha * I  # initial inverse guess
    R = I - A @ X  # residual matrix

    iterations = [X.copy()]

    for k in range(max_iter):
        X = X @ (I + R)  # update inverse approximation
        R = I - A @ X  # update residual
        iterations.append(X.copy())
        if np.linalg.norm(R, ord=np.inf) < tol:
            return X, k + 1, iterations
    return X, max_iter, iterations


# function to execute calculations
def execute_calculations():
    try:
        entries = [entry_a11, entry_a12, entry_a13, entry_a21, entry_a22, entry_a23, entry_a31, entry_a32, entry_a33]
        for entry in entries:
            if not entry.get().strip():
                raise ValueError("All fields must be filled with valid numbers.")

        A = np.array([
            [float(entry_a11.get()), float(entry_a12.get()), float(entry_a13.get())],
            [float(entry_a21.get()), float(entry_a22.get()), float(entry_a23.get())],
            [float(entry_a31.get()), float(entry_a32.get()), float(entry_a33.get())]
        ])

        inverse_A, iterations, iter_values = iterative_matrix_inverse(A)

        # display results
        result_text.set(f"Inverse Matrix (Approx.):\n{inverse_A}\nIterations: {iterations}")

        # plot the convergence of elements of inverse matrix
        fig = Figure(figsize=(8, 5))
        ax = fig.add_subplot(111)
        iter_array = np.array(iter_values)

        for i in range(iter_array.shape[1]):
            for j in range(iter_array.shape[2]):
                ax.plot(range(1, iter_array.shape[0] + 1), iter_array[:, i, j], label=f'X({i + 1},{j + 1})')

        ax.set_xlabel('Iteration')
        ax.set_ylabel('Value')
        ax.set_title('Convergence of Matrix Elements')
        ax.legend()
        ax.grid(True)

        # display the plot in the tkinter window
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=8, column=0, columnspan=6, padx=5, pady=5)

    except ValueError as e:
        result_text.set(f"Invalid input: {e}")
    except Exception as e:
        result_text.set(f"An error occurred: {e}")


# function to use predefined data
def use_predefined_data():
    predefined_values = [[5, -3, 2], [-3, 9, -1], [2, -1, 7]]
    entries = [[entry_a11, entry_a12, entry_a13], [entry_a21, entry_a22, entry_a23], [entry_a31, entry_a32, entry_a33]]

    for i in range(3):
        for j in range(3):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(0, str(predefined_values[i][j]))
    execute_calculations()


# set up the GUI
root = tk.Tk()
root.title("Computational Mathematics - Task 4")

# input fields for matrix elements
entries = []
for i in range(3):
    row_entries = []
    for j in range(3):
        entry = tk.Entry(root)
        entry.grid(row=i, column=j, padx=5, pady=5)
        row_entries.append(entry)
    entries.append(row_entries)

entry_a11, entry_a12, entry_a13 = entries[0]
entry_a21, entry_a22, entry_a23 = entries[1]
entry_a31, entry_a32, entry_a33 = entries[2]

# execute button
execute_button = tk.Button(root, text="Execute", command=execute_calculations)
execute_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# predefined data button
predefined_button = tk.Button(root, text="Use Predefined Data", command=use_predefined_data)
predefined_button.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# result display
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

# run the GUI loop
root.mainloop()