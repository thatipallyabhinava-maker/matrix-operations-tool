
import tkinter as tk
from tkinter import messagebox
import numpy as np


# Get matrix from input
def get_matrix(box):
    text = box.get("1.0", tk.END).strip()

    if text == "":
        raise ValueError("Please enter a matrix.")

    rows = text.split("\n")
    matrix = []

    for row in rows:
        numbers = row.split()

        if len(numbers) == 0:
            raise ValueError("Please do not leave empty rows.")

        try:
            matrix.append([float(x) for x in numbers])
        except ValueError:
            raise ValueError("Enter numbers only in the matrix.")

    # Check whether all rows have equal columns
    columns = len(matrix[0])

    for row in matrix:
        if len(row) != columns:
            raise ValueError(
                "Every row must have the same number of values."
            )

    return np.array(matrix)


# Display result
def show_result(result):
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, str(result))


# Addition
def addition():
    try:
        A = get_matrix(matrixA)
        B = get_matrix(matrixB)

        if A.shape != B.shape:
            raise ValueError(
                "Addition requires matrices of the same size."
            )

        result = A + B
        show_result(result)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))


# Subtraction
def subtraction():
    try:
        A = get_matrix(matrixA)
        B = get_matrix(matrixB)

        if A.shape != B.shape:
            raise ValueError(
                "Subtraction requires matrices of the same size."
            )

        result = A - B
        show_result(result)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))


# Multiplication
def multiplication():
    try:
        A = get_matrix(matrixA)
        B = get_matrix(matrixB)

        if A.shape[1] != B.shape[0]:
            raise ValueError(
                "Columns of A must equal rows of B."
            )

        result = A @ B
        show_result(result)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))


# Transpose
def transpose():
    try:
        A = get_matrix(matrixA)

        result = A.T
        show_result(result)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))


# Determinant
def determinant():
    try:
        A = get_matrix(matrixA)

        if A.shape[0] != A.shape[1]:
            raise ValueError(
                "Determinant requires a square matrix."
            )

        result = np.linalg.det(A)
        show_result(round(result, 2))

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

    except np.linalg.LinAlgError:
        messagebox.showerror(
            "Calculation Error",
            "Could not calculate the determinant."
        )


# Clear
def clear():
    matrixA.delete("1.0", tk.END)
    matrixB.delete("1.0", tk.END)
    result_box.delete("1.0", tk.END)


# Main window
window = tk.Tk()
window.title("Matrix Operations Tool")
window.geometry("600x700")


# Title
tk.Label(
    window,
    text="Matrix Operations Tool",
    font=("Arial", 20, "bold")
).pack(pady=15)


# Matrix A
tk.Label(window, text="Enter Matrix A").pack()

matrixA = tk.Text(window, height=5, width=30)
matrixA.pack(pady=5)


# Matrix B
tk.Label(window, text="Enter Matrix B").pack()

matrixB = tk.Text(window, height=5, width=30)
matrixB.pack(pady=5)


# Instructions
tk.Label(
    window,
    text="Enter numbers separated by spaces.\n"
         "Write each row on a new line.\n"
         "Example:\n1 2\n3 4"
).pack(pady=5)


# Buttons
tk.Button(
    window, text="Addition", width=18,
    command=addition
).pack(pady=3)

tk.Button(
    window, text="Subtraction", width=18,
    command=subtraction
).pack(pady=3)

tk.Button(
    window, text="Multiplication", width=18,
    command=multiplication
).pack(pady=3)

tk.Button(
    window, text="Transpose A", width=18,
    command=transpose
).pack(pady=3)

tk.Button(
    window, text="Determinant A", width=18,
    command=determinant
).pack(pady=3)

tk.Button(
    window, text="Clear", width=18,
    command=clear
).pack(pady=3)


# Result
tk.Label(
    window, text="Result",
    font=("Arial", 12, "bold")
).pack(pady=10)

result_box = tk.Text(window, height=7, width=40)
result_box.pack()


# Start application
window.mainloop()
