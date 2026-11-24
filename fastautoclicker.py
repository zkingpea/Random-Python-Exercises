from pynput.mouse import Controller, Button
import keyboard
import threading
import time
import sys

mouse = Controller()
clicking = False
click_delay = 0.05
running = True

def click_loop():
    while running:
        if clicking:
            mouse.click(Button.left)
            time.sleep(click_delay)
        else:
            time.sleep(0.01)

def toggle_clicking():
    global clicking
    clicking = not clicking
    print("Clicking:", "ON" if clicking else "OFF")

def increase_speed():
    global click_delay
    click_delay = max(0.001, click_delay - 0.005)
    print(f"Click speed increased: {click_delay:.3f}s per click")

def decrease_speed():
    global click_delay
    click_delay += 0.005
    print(f"Click speed decreased: {click_delay:.3f}s per click")

def stop_program():
    global running
    running = False
    keyboard.unhook_all()
    print("Exiting...")
    sys.exit()

# Hotkeys
keyboard.add_hotkey("shift+z", toggle_clicking)
keyboard.add_hotkey("up", increase_speed)
keyboard.add_hotkey("down", decrease_speed)
keyboard.add_hotkey("esc", stop_program)

# Start the click loop in a separate thread
threading.Thread(target=click_loop, daemon=True).start()

print("Press Shift+Z to toggle clicking. Press Esc to exit.")

# Keep program alive for hotkeys
keyboard.wait()