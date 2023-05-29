import customtkinter

# Defining basic parameters, appearance, and default color
customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('dark-blue')

# Box
root = customtkinter.CTk()
root.geometry('500x350')

# Function inside it
def add_water(index):
    fill_color = canvas.itemcget(rectangles[index], 'fill')
    if fill_color == 'grey':
        canvas.itemconfig(rectangles[index], fill='blue')
    else:
        canvas.itemconfig(rectangles[index], fill='grey')

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

# Label to take entries
label = customtkinter.CTkLabel(master=frame, text='Wasser', font=('Arial', 24))
label.pack(pady=12, padx=10)

canvas = customtkinter.CTkCanvas(root, width=500, height=350)
canvas.pack(pady=20)

# Split canvas into 14 rectangles - 250ml of water each
rectangles = []
for i in range(14):
    x1 = i * 500 // 14
    x2 = (i + 1) * 500 // 14
    rectangle = canvas.create_rectangle(x1, 0, x2, 350, fill='grey')
    rectangles.append(rectangle)

button = customtkinter.CTkButton(master=frame, text='Add Water', command=lambda: [add_water(i) for i in range(14)])
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text='Send notifications')
checkbox.pack(pady=12, padx=10)

root.mainloop()