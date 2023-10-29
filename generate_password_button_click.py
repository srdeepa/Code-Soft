import random
import string
import tkinter as tk

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_button_click():
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            result_label.config(text="Password length must be greater than 0.")
        else:
            password = generate_password(password_length)
            result_label.config(text="Generated Password: " + password)
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number for password length.")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create and place widgets
length_label = tk.Label(window, text="Enter the desired password length:")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_password_button_click)
generate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI application
window.mainloop()
