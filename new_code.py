import tkinter as tk
from tkinter import messagebox

def calculate():
    """Calculate BMI and display result with category"""
    try:
        # ✅ PERBAIKAN: Ambil weight dari weigh_ent dan height dari height_ent
        weight = float(weigh_ent.get())
        height = float(height_ent.get())  # ← INI YANG DIPERBAIKI!
        
        # Validasi input
        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and height must be positive numbers!")
            return
        
        if height > 3:  # Asumsi tinggi dalam meter, bukan cm
            messagebox.showwarning("Warning", "Height seems too high. Use meters (e.g., 1.75)")
            return

        # Hitung BMI
        bmi = weight / (height ** 2)
        bmi = round(bmi, 1)

        # Tentukan kategori dan warna
        if bmi < 18.5:
            category = "UnderWeight"
            advice = "You need to gain weight"
            color = "#3498db"  # Blue
            
        elif 18.5 <= bmi <= 24.9:
            category = "Normal"
            advice = "You're doing great!"
            color = "#2ecc71"  # Green
            
        elif 25 <= bmi <= 29.9:
            category = "OverWeight"
            advice = "You need to lose weight"
            color = "#f39c12"  # Orange
            
        elif 30 <= bmi <= 34.9:
            category = "Obese"
            advice = "You should lose weight"
            color = "#e74c3c"  # Red
            
        else:  # bmi >= 35
            category = "Extremely Obese"
            advice = "You must lose weight (consult a doctor)"
            color = "#c0392b"  # Dark Red

        # Update hasil
        result_var.set(f"Your BMI: {bmi}\nCategory: {category}\n{advice}")
        result_lbl.config(fg=color, font=('Arial', 11, 'bold'))
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Height cannot be zero!")

def clear_fields():
    """Clear all input fields and result"""
    weigh_ent.delete(0, tk.END)
    height_ent.delete(0, tk.END)
    result_var.set('')
    weigh_ent.focus()

def on_enter(event):
    """Handle Enter key press"""
    calculate()

# Setup window
root = tk.Tk()
root.title('BMI Calculator')
root.geometry('400x350')
root.config(padx=30, pady=30, bg='#ecf0f1')
root.resizable(False, False)

# Header
header_lbl = tk.Label(
    root,
    text='BMI CALCULATOR',
    font=('Arial', 18, 'bold'),
    bg='#ecf0f1',
    fg='#2c3e50'
)
header_lbl.grid(columnspan=2, row=0, pady=(0, 20))

# Weight label and entry
weight_lbl = tk.Label(
    root,
    text='Weight (kg):',
    font=('Arial', 12),
    bg='#ecf0f1',
    fg='#34495e'
)
weight_lbl.grid(column=0, row=1, sticky='w', pady=10)

weigh_ent = tk.Entry(
    root,
    font=('Arial', 12),
    width=15,
    relief=tk.GROOVE,
    bd=2
)
weigh_ent.grid(column=1, row=1, pady=10, padx=(10, 0))
weigh_ent.bind('<Return>', on_enter)
weigh_ent.focus()

# Height label and entry
height_lbl = tk.Label(
    root,
    text='Height (m):',
    font=('Arial', 12),
    bg='#ecf0f1',
    fg='#34495e'
)
height_lbl.grid(column=0, row=2, sticky='w', pady=10)

height_ent = tk.Entry(
    root,
    font=('Arial', 12),
    width=15,
    relief=tk.GROOVE,
    bd=2
)
height_ent.grid(column=1, row=2, pady=10, padx=(10, 0))
height_ent.bind('<Return>', on_enter)

# Buttons frame
button_frame = tk.Frame(root, bg='#ecf0f1')
button_frame.grid(columnspan=2, row=3, pady=20)

# Calculate button
submit_butn = tk.Button(
    button_frame,
    text='Calculate',
    font=('Arial', 12, 'bold'),
    bg='#3498db',
    fg='white',
    command=calculate,
    width=12,
    relief=tk.RAISED,
    bd=3,
    cursor='hand2'
)
submit_butn.pack(side=tk.LEFT, padx=5)

# Clear button
clear_butn = tk.Button(
    button_frame,
    text='Clear',
    font=('Arial', 12, 'bold'),
    bg='#95a5a6',
    fg='white',
    command=clear_fields,
    width=12,
    relief=tk.RAISED,
    bd=3,
    cursor='hand2'
)
clear_butn.pack(side=tk.LEFT, padx=5)

# Result label
result_var = tk.StringVar(value='')
result_lbl = tk.Label(
    root,
    textvariable=result_var,
    font=('Arial', 11),
    bg='#ecf0f1',
    fg='#2c3e50',
    justify=tk.LEFT,
    wraplength=350
)
result_lbl.grid(columnspan=2, row=4, pady=20)

# Info label
info_lbl = tk.Label(
    root,
    text='BMI Categories:\n'
         'Below 18.5 = Underweight\n'
         '18.5 - 24.9 = Normal\n'
         '25.0 - 29.9 = Overweight\n'
         '30.0 - 34.9 = Obese\n'
         'Above 35.0 = Extremely Obese',
    font=('Arial', 8),
    bg='#ecf0f1',
    fg='#7f8c8d',
    justify=tk.LEFT
)
info_lbl.grid(columnspan=2, row=5, pady=(10, 0))

root.mainloop()
