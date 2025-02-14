import tkinter as tk
from tkinter import ttk
import subprocess

def open_task(task_number):
    subprocess.Popen(['python', f'task{task_number}.py'])

# Set up the GUI
root = tk.Tk()
root.title("Task Selection Menu")
root.geometry("400x500")

task_names = [
    "Task 1: Graphical Method and Absolute Error",
    "Task 2: Comparison of Root-Finding Methods",
    "Task 3: Jacobi Method",
    "Task 4: Iterative Method for Matrix Inversion",
    "Task 5: Linear Curve Fitting",
    "Task 6: First Derivative Using Newton’s Forward Difference Formula",
    "Task 7: Taylor Series Method",
    "Task 8: Simpson’s 3/8 Rule"
]

for i, task_name in enumerate(task_names, start=1):
    task_button = tk.Button(root, text=task_name, command=lambda i=i: open_task(i))
    task_button.grid(row=i-1, column=0, padx=20, pady=10, sticky="ew")

root.mainloop()