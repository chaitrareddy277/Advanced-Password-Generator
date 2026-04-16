import tkinter as tk
from tkinter import messagebox
import secrets
import string
def generate_password():
    try:
        length = int(length_entry.get())
        exclude = exclude_entry.get()
        if length < 8:
            messagebox.showerror("Error", "Password length must be at least 8")
            return
        chars = ""
        if var_upper.get():
            chars += string.ascii_uppercase
        if var_lower.get():
            chars += string.ascii_lowercase
        if var_digits.get():
            chars += string.digits
        if var_symbols.get():
            chars += string.punctuation
        if not chars:
            messagebox.showerror("Error", "Select at least one character set")
            return
        for c in exclude:
            chars = chars.replace(c, "")
        if not chars:
            messagebox.showerror("Error", "All characters excluded")
            return
        password = []
        if var_upper.get():
            password.append(secrets.choice(string.ascii_uppercase))
        if var_lower.get():
            password.append(secrets.choice(string.ascii_lowercase))
        if var_digits.get():
            password.append(secrets.choice(string.digits))
        if var_symbols.get():
            password.append(secrets.choice(string.punctuation))
        while len(password) < length:
            password.append(secrets.choice(chars))
        secrets.SystemRandom().shuffle(password)
        password = ''.join(password)
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Invalid password length")
def copy_to_clipboard():
    password = result_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard")
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("420x450")
tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)
tk.Label(root, text="Password Length").pack()
length_entry = tk.Entry(root)
length_entry.insert(0, "12")
length_entry.pack()
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=var_upper).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=var_lower).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Include Digits (0-9)", variable=var_digits).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Include Symbols (!@#$)", variable=var_symbols).pack(anchor="w", padx=40)
tk.Label(root, text="Exclude Characters (optional)").pack(pady=5)
exclude_entry = tk.Entry(root)
exclude_entry.pack()
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
result_entry = tk.Entry(root, font=("Arial", 12), width=30)
result_entry.pack(pady=10)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)
root.mainloop()