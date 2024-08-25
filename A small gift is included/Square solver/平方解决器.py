import tkinter as tk
from tkinter import messagebox

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i == 0:
            n //= i
            factors.append(i)
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors

def factorize_to_text(factors):
    factor_counts = {}
    for factor in factors:
        factor_counts[factor] = factor_counts.get(factor, 0) + 1
    output = ""
    for factor, count in factor_counts.items():
        if output:
            output += " * "
        output += f"{factor}^{count}"
    return output

def calculate_factors():
    try:
        X = int(entry.get())
        if X <= 0:
            messagebox.showerror("Error", "Please enter a positive number!")
        else:
            factors = prime_factors(X)
            result = factorize_to_text(factors)
            result_text = f"The prime factorization of {X} is: {result}\n"
            result_label.config(text=result_text)
            history_text.insert(tk.END, result_text)
            history_text.see(tk.END)  # Scroll to the end of the text
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

def clear_history():
    history_text.delete(1.0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Prime Factorization")

# Create a frame for the input field and buttons
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create an entry widget for the user input
entry = tk.Entry(frame, width=20)
entry.pack(side=tk.LEFT, padx=(0, 10))

# Create a button to trigger the calculation
calculate_button = tk.Button(frame, text="Calculate", command=calculate_factors)
calculate_button.pack(side=tk.LEFT)

# Create a button to clear the history
clear_button = tk.Button(frame, text="Clear History", command=clear_history)
clear_button.pack(side=tk.LEFT, padx=(10, 0))

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Create a frame for the text widget and scrollbar
history_frame = tk.Frame(root)
history_frame.pack(pady=10)

# Create a text widget to display the history of results
history_text = tk.Text(history_frame, height=10, width=50)
history_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollbar widget and associate it with the text widget
scrollbar = tk.Scrollbar(history_frame, command=history_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the text widget to use the scrollbar
history_text.config(yscrollcommand=scrollbar.set)

# Bind the window closing event to a custom function
root.protocol("WM_DELETE_WINDOW", root.destroy)

# Start the GUI event loop
root.mainloop()
