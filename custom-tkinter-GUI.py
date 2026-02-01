"""
BMI Calculator with CustomTkinter Library's 
You first must be to installed: Customtkinter with command => 'pip install customtkinter'
"""

import customtkinter as ctk
from tkinter import messagebox

def calculate():
    """Calculate BMI and display result with category"""
    try:
        weight = float(weigh_ent.get())
        height = float(height_ent.get())
        
        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and height must be positive!")
            return
        
        if height > 3:
            messagebox.showwarning("Warning", "Height seems too high. Use meters (e.g., 1.75)")
            return

        bmi = weight / (height ** 2)
        bmi = round(bmi, 1)

        if bmi < 18.5:
            category = "UnderWeight"
            advice = "You need to gain weight"
            color = "#3498db"
            
        elif 18.5 <= bmi <= 24.9:
            category = "Normal"
            advice = "You're doing great!"
            color = "#2ecc71"
            
        elif 25 <= bmi <= 29.9:
            category = "OverWeight"
            advice = "You need to lose weight"
            color = "#f39c12"
            
        elif 30 <= bmi <= 34.9:
            category = "Obese"
            advice = "You should lose weight"
            color = "#e74c3c"
            
        else:
            category = "Extremely Obese"
            advice = "You must lose weight"
            color = "#c0392b"

        result_lbl.configure(
            text=f"Your BMI: {bmi}\nCategory: {category}\n{advice}",
            text_color=color
        )
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

def clear_fields():
    """Clear all input fields"""
    weigh_ent.delete(0, 'end')
    height_ent.delete(0, 'end')
    result_lbl.configure(text='')
    weigh_ent.focus()

# Setup CustomTkinter
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

root = ctk.CTk()
root.title('BMI Calculator')
root.geometry('450x500')
root.resizable(False, False)

# Header
header = ctk.CTkLabel(
    root,
    text='BMI CALCULATOR',
    font=('Arial', 28, 'bold')
)
header.pack(pady=30)

# Input frame
input_frame = ctk.CTkFrame(root)
input_frame.pack(pady=20, padx=40, fill='x')

# Weight
weight_lbl = ctk.CTkLabel(
    input_frame,
    text='Weight (kg):',
    font=('Arial', 16)
)
weight_lbl.grid(row=0, column=0, padx=20, pady=15, sticky='w')

weigh_ent = ctk.CTkEntry(
    input_frame,
    placeholder_text='Enter weight',
    font=('Arial', 14),
    width=200
)
weigh_ent.grid(row=0, column=1, padx=20, pady=15)

# Height
height_lbl = ctk.CTkLabel(
    input_frame,
    text='Height (m):',
    font=('Arial', 16)
)
height_lbl.grid(row=1, column=0, padx=20, pady=15, sticky='w')

height_ent = ctk.CTkEntry(
    input_frame,
    placeholder_text='Enter height',
    font=('Arial', 14),
    width=200
)
height_ent.grid(row=1, column=1, padx=20, pady=15)

# Buttons
button_frame = ctk.CTkFrame(root, fg_color='transparent')
button_frame.pack(pady=20)

calculate_btn = ctk.CTkButton(
    button_frame,
    text='Calculate BMI',
    command=calculate,
    font=('Arial', 16, 'bold'),
    width=150,
    height=40
)
calculate_btn.pack(side='left', padx=10)

clear_btn = ctk.CTkButton(
    button_frame,
    text='Clear',
    command=clear_fields,
    font=('Arial', 16, 'bold'),
    width=150,
    height=40,
    fg_color='#95a5a6',
    hover_color='#7f8c8d'
)
clear_btn.pack(side='left', padx=10)

# Result
result_lbl = ctk.CTkLabel(
    root,
    text='',
    font=('Arial', 16, 'bold'),
    justify='left'
)
result_lbl.pack(pady=20)

# Info
info_frame = ctk.CTkFrame(root)
info_frame.pack(pady=10, padx=40, fill='x')

info_text = """BMI Categories:
• Below 18.5 = Underweight
• 18.5 - 24.9 = Normal
• 25.0 - 29.9 = Overweight
• 30.0 - 34.9 = Obese
• Above 35.0 = Extremely Obese"""

info_lbl = ctk.CTkLabel(
    info_frame,
    text=info_text,
    font=('Arial', 11),
    justify='left'
)
info_lbl.pack(pady=15, padx=20)

weigh_ent.focus()

root.mainloop()
