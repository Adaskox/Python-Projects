import pyautogui
import time
import keyboard

def wait_for_button(image_path, timeout=30, confidence=0.95):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            x, y, _, _ = pyautogui.locateOnScreen(image_path, confidence=confidence)
            print(f"Button found at ({x}, {y})")
            return x, y
        except Exception:
            time.sleep(1)

    print(f"{image_path} not found within the timeout.")
    return None

def click_on_button(x, y):
    pyautogui.moveTo(x, y, duration=0.25)
    pyautogui.click()
    print(f"Clicked on the button at ({x}, {y})")

# Place your own paths to png's here:
button_image_vortex = r'C:\Users\Adaskox\Desktop\Programowanie\Projekty\NexusAutoDownload\Vortex.png'
button_image_nexus = r'C:\Users\Adaskox\Desktop\Programowanie\Projekty\NexusAutoDownload\Nexus.png'

i = 0
while i < 10:
    print('Waiting for Vortex download button...')
    vortex_position = wait_for_button(button_image_vortex)
    if vortex_position is not None:
        click_on_button(*vortex_position)
        time.sleep(3)

        print('Waiting for Nexus download button...')
        nexus_position = wait_for_button(button_image_nexus)
        if nexus_position is not None:
            click_on_button(*nexus_position)

        time.sleep(0.2)
        print("Closing page")
        keyboard.press_and_release('left ctrl+w')
        time.sleep(1)
