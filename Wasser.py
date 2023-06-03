import os
import customtkinter
from winreg import HKEY_CURRENT_USER, REG_SZ, SetValueEx, OpenKey, CloseKey, KEY_ALL_ACCESS, KEY_WRITE, KEY_READ, \
    DeleteValue
from win10toast import ToastNotifier
import threading
import time

# Define basic parameters, appearance, and default color
customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('dark-blue')

# Box
root = customtkinter.CTk()
root.minsize(300, 700)
root.geometry('300x700')

choice = [3000]
start_with_windows = False
send_notifications = False

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

    start_with_win_checkbox = customtkinter.CTkCheckBox(master=settings_window, text='Start with Windows', command=None)
    start_with_win_checkbox.pack(pady=10)

    def apply():
        global choice, start_with_windows, send_notifications
        ml = int(int(choice[0]) / 250)

        # Split canvas into 'ml' rectangles - 250ml of water each
        for rectangle in rectangles:
            canvas.delete(rectangle)  # Remove previous rectangles

        rectangles.clear()  # Clear the list of rectangles

        for i in range(ml):
            y2 = 350 - (i * 350 // ml)
            y1 = 350 - ((i + 1) * 350 // ml)
            rectangle = canvas.create_rectangle(0, y1, 200, y2, fill='grey')
            rectangles.append(rectangle)

        volume = 500
        for i in range(len(rectangles)):
            if i % 2 == 1:
                y1 = 350 - (i * 350 // ml)
                y2 = 350 - ((i + 1) * 350 // ml)
                text = canvas.create_text(100, (y1 + y2) // 2, text=f'{volume}ml', fill='white')
                volume += 500

        # Update the start_with_windows and send_notifications variables
        start_with_windows = start_with_win_checkbox.get()
        send_notifications = notifications_checkbox.get()

        # Apply the changes
        apply_settings()

    def apply_settings():
        # Apply the start_with_windows setting
        if start_with_windows:
            # Get the path to the script
            script_path = os.path.abspath(__file__)

            # Add the script to the startup list
            add_to_startup(script_path)
        else:
            # Remove the script from the startup list
            remove_from_startup()

        # Start or stop the notification thread based on the send_notifications setting
        if send_notifications:
            start_notification_thread()
        else:
            stop_notification_thread()

    def add_to_startup(path):
        # Open the registry key for the current user's startup programs
        key = OpenKey(HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 0, KEY_ALL_ACCESS)

        # Set the path of the script as the value
        SetValueEx(key, 'WasserApp', 0, REG_SZ, path)

        # Close the registry key
        CloseKey(key)

    def remove_from_startup():
        # Open the registry key for the current user's startup programs
        key = OpenKey(HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', 0, KEY_ALL_ACCESS)

        try:
            # Delete the value associated with the script
            DeleteValue(key, 'WasserApp')
        except FileNotFoundError:
            # The script was not found in the startup programs
            pass

        # Close the registry key
        CloseKey(key)

    def show_notification():
        toaster = ToastNotifier()
        toaster.show_toast("Reminder", "Remember to drink water", duration=10)

    def start_notification_thread():
        def run_notification_thread():
            while send_notifications:
                # Show the notification
                show_notification()

                # Sleep for 1 hour (3600 seconds)
                time.sleep(3600)

        # Create and start the notification thread
        notification_thread = threading.Thread(target=run_notification_thread)
        notification_thread.start()

    def stop_notification_thread():
        global send_notifications
        # Set send_notifications to False to stop the thread
        send_notifications = False

    apply_button = customtkinter.CTkButton(master=settings_window, text='Apply', command=apply)
    apply_button.pack(pady=10)

    combobox = customtkinter.CTkOptionMenu(master=settings_window,
                                           values=["3000", "4000", "5000"],
                                           command=lambda value: choice.__setitem__(0, int(value)))
    combobox.pack(pady=10)
    combobox.set(str(choice[0]))  # set initial value

    settings_window.mainloop()

    # After the settings window is closed, continue the main application
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

ml = int(int(choice[0]) / 250)

# Split canvas into 'ml' rectangles - 250ml of water each
rectangles = []
for i in range(ml):
    y2 = 350 - (i * 350 // ml)
    y1 = 350 - ((i + 1) * 350 // ml)
    rectangle = canvas.create_rectangle(0, y1, 200, y2, fill='grey')
    rectangles.append(rectangle)

volume = 500
for i in range(len(rectangles)):
    if i % 2 == 1:
        y1 = 350 - (i * 350 // ml)
        y2 = 350 - ((i + 1) * 350 // ml)
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
