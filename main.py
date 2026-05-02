import tkinter as tk
import re

def check_password_strenth(password):
    if len(password) < 8:
        return "Weak: At least 8 characters needed"
    if not any(char.isdigit() for char in password):
        return "Weak: Must contain a digit"
    if not any(char.isupper() for char in password):
        return "Weak: Must have an uppercase letter"
    if not any(char.islower() for char in password):
        return "Weak: Must have a lowercase letter"
    if not re.search(r'[!@#$%^&*]', password):
        return "Weak: Must have a special character"
    return "Strong: Your password is secure ✅"

def check_password():
    password = entry.get()
    result = check_password_strenth(password)
    result_label.config(text=result)

# Window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x400")
root.configure(bg="lightblue")

# 👉 CENTER FRAME
frame = tk.Frame(root, bg="lightblue")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Widgets inside frame
title = tk.Label(frame, text="Password Strength Checker",font=("Calibri", 14,"bold"), bg="lightblue")
title.pack(pady=10)

entry = tk.Entry(frame, width=30, show="*", font=("Arial", 14))
entry.pack(pady=10)

check_btn = tk.Button(frame, text="Check Password",command=check_password)
check_btn.pack(pady=10)

result_label = tk.Label(frame, text="",font=("Arial", 16), bg="lightblue")
result_label.pack(pady=10)

root.mainloop()