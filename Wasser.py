import customtkinter

# Defining basic parameters, appearance, and default color
customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('dark-blue')

# Box
root = customtkinter.CTk()
root.geometry('500x750')

# Function inside it
def add_water():
    if canvas.itemcget(rectangles[active_rectangle[0]], 'fill') == 'grey':
        canvas.itemconfig(rectangles[active_rectangle[0]], fill='blue')
        active_rectangle[0] = (active_rectangle[0] - 1) % len(rectangles)
    elif all(canvas.itemcget(rectangle, 'fill') == 'blue' for rectangle in rectangles):
        # All rectangles are already blue, do nothing
        pass
    else:
        # Find the first grey rectangle and color it blue
        for rectangle in rectangles:
            if canvas.itemcget(rectangle, 'fill') == 'grey':
                canvas.itemconfig(rectangle, fill='blue')
                active_rectangle[0] = (active_rectangle[0] - 1) % len(rectangles)
                break

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

# Label to take entries
label = customtkinter.CTkLabel(master=frame, text='Wasser', font=('Arial', 24))
label.pack(pady=12, padx=10)

canvas = customtkinter.CTkCanvas(root, width=200, height=400)
canvas.pack(pady=20)

# Split canvas into 14 rectangles - 250ml of water each
rectangles = []
for i in range(14):
    y1 = (i + 1) * 350 // 14
    y2 = (i + 2) * 350 // 14
    rectangle = canvas.create_rectangle(0, y1, 200, y2, fill='grey')
    rectangles.append(rectangle)

active_rectangle = [len(rectangles) - 1]  # Start from the third last rectangle index

button = customtkinter.CTkButton(master=frame, text='Add Water', command=add_water)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text='Send notifications')
checkbox.pack(pady=12, padx=10)

root.mainloop()
