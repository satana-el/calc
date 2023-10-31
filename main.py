import tkinter as tk

# create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x400")

# Disaple resizing
root.minsize(400, 500)
root.maxsize(400, 500)

# Entry for displaying the equation
equation_var = tk.StringVar()
equation_box = tk.Entry(root, textvariable=equation_var, font=("Helvetica", 25), justify="right", bd=2)
equation_box.grid(row=0, column=0, columnspan=4, rowspan=2, sticky="nsew")

# Buttons
# Operators
plus = tk.Button(root, text="+", font=("Helvetica", 16), width = 5, height = 3)
minus = tk.Button(root, text="-", font=("Helvetica", 16), width = 5, height = 3)
multi = tk.Button(root, text="×", font=("Helvetica", 16), width = 5, height = 3)
div = tk.Button(root, text="÷", font=("Helvetica", 16), width = 5, height = 3)
equals = tk.Button(root, text="=", font=("Helvetica", 16), width = 5, height = 3)
dot = tk.Button(root, text=".", font=("Helvetica", 16), width = 5, height = 3)

# Numbers
seven = tk.Button(root, text="7", font=("Helvetica", 16), width = 5, height = 3)
eight = tk.Button(root, text="8", font=("Helvetica", 16), width = 5, height = 3)
nine = tk.Button(root, text="9", font=("Helvetica", 16), width = 5, height = 3)
four = tk.Button(root, text="4", font=("Helvetica", 16), width = 5, height = 3)
five = tk.Button(root, text="5", font=("Helvetica", 16), width = 5, height = 3)
six= tk.Button(root, text="6", font=("Helvetica", 16), width = 5, height = 3)
one = tk.Button(root, text="1", font=("Helvetica", 16), width = 5, height = 3)
two= tk.Button(root, text="2", font=("Helvetica", 16), width = 5, height = 3)
three = tk.Button(root, text="3", font=("Helvetica", 16), width = 5, height = 3)
zero = tk.Button(root, text="0", font=("Helvetica", 16), width = 5, height = 3)

# Put the buttons on the grid.
plus.grid(row=2, column=3, padx=5, pady=3)
minus.grid(row=3, column=3, padx=5, pady=3)
multi.grid(row=4, column=3, padx=5, pady=3)
div.grid(row=5, column=3, padx=5, pady=3)
equals.grid(row=5, column=2, padx=5, pady=3)
dot.grid(row=5, column=1, padx=5, pady=3)

seven.grid(row=2, column=0, padx=5, pady=3)
eight.grid(row=2, column=1, padx=5, pady=3)
nine.grid(row=2, column=2, padx=5, pady=3)
four.grid(row=3, column=0, padx=5, pady=3)
five.grid(row=3, column=1, padx=5, pady=3)
six.grid(row=3, column=2, padx=5, pady=3)
one.grid(row=4, column=0, padx=5, pady=3)
two.grid(row=4, column=1, padx=5, pady=3)
three.grid(row=4, column=2, padx=5, pady=3)
zero.grid(row=5, column=0, padx=5, pady=3)

# Configure row and column weights to make the grid cells expandable
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)


# Start the main event loop
root.mainloop()

