import customtkinter

# Defining basic parameters, appearance, and default color
customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('dark-blue')

# Box
root = customtkinter.CTk()
root.minsize(300, 700)
root.geometry('300x700')

# Function inside it
def add_water():
    if active_rectangle[0] < len(rectangles):
        canvas.itemconfig(rectangles[active_rectangle[0]], fill='DeepSkyBlue3')
        active_rectangle[0] += 1

def subtract_water():
    if active_rectangle[0] > 0:
        active_rectangle[0] -= 1
        canvas.itemconfig(rectangles[active_rectangle[0]], fill='grey')

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

# Label to take entries
label = customtkinter.CTkLabel(master=frame, text='Wasser', font=('Arial', 24))
label.pack(pady=12, padx=10)

canvas = customtkinter.CTkCanvas(root, width=200, height=350)
canvas.pack(pady=20)

# Split canvas into 14 rectangles - 250ml of water each
rectangles = []
for i in range(14):
    y2 = 350 - (i * 350 // 14)
    y1 = 350 - ((i + 1) * 350 // 14)
    rectangle = canvas.create_rectangle(0, y1, 200, y2, fill='grey')
    rectangles.append(rectangle)

volume = 500
for i in range(len(rectangles)):
    if i % 2 == 1:
        y1 = 350 - (i * 350 // 14)
        y2 = 350 - ((i + 1) * 350 // 14)
        text = canvas.create_text(100, (y1 + y2) // 2, text=f'{volume}ml', fill='white')
        volume += 500

active_rectangle = [0]  # Start from the first rectangle index

button = customtkinter.CTkButton(master=frame, text='Add Water', command=add_water)
button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text='Remove Water', command=subtract_water)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text='Send notifications')
checkbox.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text='Apply')
button.pack(pady=12, padx=10)

root.mainloop()
