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

def open_settings_window():
    settings_window = customtkinter.CTk()
    settings_window.geometry('300x250')
    settings_window.title('Settings')

    settings_label = customtkinter.CTkLabel(master=settings_window, text='Settings', font=('Arial', 16))
    settings_label.pack(pady=20)

    notifications_checkbox = customtkinter.CTkCheckBox(master=settings_window, text='Send notifications', command=None)
    notifications_checkbox.pack(pady=10)

    startwithwin_checkbox = customtkinter.CTkCheckBox(master=settings_window, text='Start with Windows', command=None)
    startwithwin_checkbox.pack(pady=10)

    apply_button = customtkinter.CTkButton(master=settings_window, text='Apply', command=None)
    apply_button.pack(pady=10)

    settings_window.mainloop()

    # After settings window is closed, continue the main application
    root.focus_set()

def quit():
    root.quit()


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

add_button = customtkinter.CTkButton(master=frame, text='Add Water', command=add_water)
add_button.pack(pady=12, padx=10)

remove_button = customtkinter.CTkButton(master=frame, text='Remove Water', command=subtract_water)
remove_button.pack(pady=12, padx=10)

settings_button = customtkinter.CTkButton(master=frame, text='Settings', command=open_settings_window)
settings_button.pack(padx=12, pady=10)

quit_button = customtkinter.CTkButton(master=frame, text='Quit', command=quit)
quit_button.pack(padx=12, pady=10)

root.mainloop()
