#calculator application
import tkinter as tk

# Function to update the display when a button is clicked
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to clear the display
def clear():
    entry.delete(0, tk.END)

# Function to perform the calculation
def calculate():
    current = entry.get()
    try:
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create a tkinter window
window = tk.Tk()
window.title("Simple Calculator")

# Create an entry widget for the display
entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons
buttons = [
    
    '7',  '8',  '9',  '/',

    '4',  '5',  '6',  '*',

    '1',  '2',  '3',  '-',

    '0',  '.',  '=',  '+'
]

# Create and place the buttons on the grid
row, col = 1, 0
for button in buttons:
    if button == '=':
        tk.Button(window, text=button, command=calculate).grid(row=row, column=col)
    elif button == 'C':
        tk.Button(window, text=button, command=clear).grid(row=row, column=col)
    else:
        tk.Button(window, text=button, command=lambda b=button: button_click(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the GUI main loop
window.mainloop()
