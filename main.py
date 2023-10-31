import tkinter as tk

def on_button_click(value):
    current_equation = equation_var.get()
    
    if value in "+-":
        equation_var.set(current_equation + f" {value} ")
    elif value == "×":
        equation_var.set(current_equation + f" * ")
    elif value == "÷" :
        equation_var.set(current_equation + f" / ")
    elif value == "=":
        result = eval(current_equation)
        equation_var.set(result)
    else:
        equation_var.set(current_equation + str(value))
 

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x400")

# Disable resizing
root.minsize(400, 500)
root.maxsize(400, 500)

# Entry for displaying the equation
equation_var = tk.StringVar()
equation_box = tk.Entry(root, textvariable=equation_var, font=("Helvetica", 25), justify="right", bd=2)
equation_box.grid(row=0, column=0, columnspan=4, rowspan=2, sticky="nsew")

# Buttons
buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "×",
    "0", ".", "=", "÷"
]

# Initailize row values, so that they don't collide with equation_box
row_val = 2
col_val = 0

# Buttons
for button_value in buttons:
    button = tk.Button(root, text=button_value, command=lambda value=button_value: on_button_click(value), font=("Helvetica", 16), width = 5, height = 3)
    button.grid(row = row_val, column=col_val, padx = 5, pady = 3)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val +=1

# Configure row and column weights to make the grid cells expandable
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)


# Start the main event loop
root.mainloop()

