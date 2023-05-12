import random
import string
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk

def generate_password(length, chars):
    """This function generates a random password based on the user-provided length and character set."""
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password

def generate():
    """This function is called when the 'Generate Password' button is clicked."""
    length = int(length_var.get())
    chars = ''
    if uppercase_var.get():
        chars += string.ascii_uppercase
    if lowercase_var.get():
        chars += string.ascii_lowercase
    if digits_var.get():
        chars += string.digits
    if punctuation_var.get():
        chars += string.punctuation
    password = generate_password(length, chars)
    password_label.config(text= password)
    copy_button.config(state="normal")
    global generated_password
    generated_password = password

def copy_to_clipboard():
    """This function is called when the 'Copy Password' button is clicked."""
    root.clipboard_clear()
    root.clipboard_append(generated_password)
    messagebox.showinfo("Password Copied", "Password has been copied to clipboard.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x300")



# Create the widgets
length_label = tk.Label(root, text="Password Length:")
length_var = tk.StringVar()
length_dropdown = ttk.Combobox(root, textvariable=length_var, values=list(range(6, 2049)))
length_dropdown.current(0)
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
punctuation_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(root, text="Use Uppercase Letters", variable=uppercase_var)
lowercase_checkbox = tk.Checkbutton(root, text="Use Lowercase Letters", variable=lowercase_var)
digits_checkbox = tk.Checkbutton(root, text="Use Digits", variable=digits_var)
punctuation_checkbox = tk.Checkbutton(root, text="Use Punctuation", variable=punctuation_var)
generate_button = tk.Button(root, text="Generate Password", command=generate)
password_label = tk.Label(root, text="")
copy_button = tk.Button(root, text="Copy Password", state="disabled", command=copy_to_clipboard)

# Add the widgets to the window
length_label.grid(row=0, column=0, sticky="W")
length_dropdown.grid(row=0, column=1, sticky="W")
uppercase_checkbox.grid(row=1, column=1, sticky="W")
lowercase_checkbox.grid(row=2, column=1, sticky="W")
digits_checkbox.grid(row=3, column=1, sticky="W")
punctuation_checkbox.grid(row=4, column=1, sticky="W")
generate_button.grid(row=5, column=1, sticky="W")
password_label.grid(row=6, column=1, sticky="W")
copy_button.grid(row=7, column=1, sticky="W")

# Start the main event loop
root.mainloop()
