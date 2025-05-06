import string
import math
import tkinter as tk
from tkinter import messagebox

# Entropy calculator
def calculate_entropy(password):
    charset = 0
    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in string.punctuation for c in password):
        charset += len(string.punctuation)
    if charset == 0:
        return 0
    return round(len(password) * math.log2(charset), 2)

# Password strength evaluator
def check_password_strength():
    password = entry.get()
    entropy = calculate_entropy(password)

    has_letter = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if len(password) < 6:
        result = "❌ Weak password: Too short.\n🔧 Suggestion: Use at least 8 characters."
    elif len(password) >= 6 and has_letter and has_digit and not has_special:
        result = "⚠️ Medium password: Add special characters (!@#$...)\n🔧 Example: " + password + "!"
    elif len(password) >= 8 and has_letter and has_digit and has_special:
        result = "✅ Strong password: Good job!"
    else:
        result = "❌ Weak password: Needs letters and numbers.\n🔧 Suggestion: Mix letters, numbers, and symbols."

    entropy_msg = f"\n🔐 Entropy: {entropy} bits"
    if entropy < 28:
        entropy_msg += " (Very Weak)"
    elif entropy < 36:
        entropy_msg += " (Weak)"
    elif entropy < 60:
        entropy_msg += " (Reasonable)"
    else:
        entropy_msg += " (Strong)"

    messagebox.showinfo("Password Check Result", result + entropy_msg)

# GUI setup
window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("400x200")

label = tk.Label(window, text="Enter your password:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(window, width=30, show="*", font=("Arial", 12))
entry.pack()

button = tk.Button(window, text="Check Strength", command=check_password_strength, font=("Arial", 12))
button.pack(pady=10)

window.mainloop()
