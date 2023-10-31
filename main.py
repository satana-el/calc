import tkinter as tk

# create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x400")

# Disaple resizing
root.minsize(400, 400)
root.maxsize(400, 400)

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



# Pack the label and button into the window
# plus.pack(side="top", padx = 5)
# minus.pack(side="top", padx = 5)
# multi.pack(side="top", padx = 5)
# div.pack(side="top", padx = 5)
# equals.pack(side="top", padx = 5)

plus.grid(row=0, column=3, padx=5, pady=3)
minus.grid(row=1, column=3, padx=5, pady=3)
multi.grid(row=2, column=3, padx=5, pady=3)
div.grid(row=3, column=3, padx=5, pady=3)
equals.grid(row=3, column=2, padx=5, pady=3)
dot.grid(row=3, column=1, padx=5, pady=3)

seven.grid(row=0, column=0, padx=5, pady=3)
eight.grid(row=0, column=1, padx=5, pady=3)
nine.grid(row=0, column=2, padx=5, pady=3)
four.grid(row=1, column=0, padx=5, pady=3)
five.grid(row=1, column=1, padx=5, pady=3)
six.grid(row=1, column=2, padx=5, pady=3)
one.grid(row=2, column=0, padx=5, pady=3)
two.grid(row=2, column=1, padx=5, pady=3)
three.grid(row=2, column=2, padx=5, pady=3)
zero.grid(row=3, column=0, padx=5, pady=3)


# Start the main event loop
root.mainloop()

