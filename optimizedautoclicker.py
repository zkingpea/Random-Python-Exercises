from pynput import mouse, keyboard
import threading
import time
import sys

# Variables
mouse_controller = mouse.Controller()
clicking = False
running = True
click_delay = 0.05


def click_loop():
    global clicking, running
    while running:
        if clicking:
            mouse_controller.click(mouse.Button.left)
            time.sleep(click_delay)
        else:
            time.sleep(0.01)


def on_press(key):
    global clicking, running, click_delay

    # --- Character keys ---
    if hasattr(key, "char") and key.char is not None:
        if key.char == 'Z':  # Shift+Z
            clicking = not clicking
            print("Clicking:", "ON" if clicking else "OFF")

    # --- Special keys ---
    if key == keyboard.Key.up:
        click_delay = max(0.001, click_delay - 0.005)
        print(f"Speed: {click_delay:.3f}s")

    elif key == keyboard.Key.down:
        click_delay += 0.005
        print(f"Speed: {click_delay:.3f}s")

    elif key == keyboard.Key.esc:
        running = False
        print("Exiting...")
        return False


# Start clicking thread
threading.Thread(target=click_loop, daemon=True).start()

print("Shift+Z = Toggle | Up/Down = Speed | Esc = Exit")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

sys.exit()