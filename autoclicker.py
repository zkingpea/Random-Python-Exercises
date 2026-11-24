import pyautogui
import keyboard
import time

clicking = False
last_state = None
click_delay = 0.1  # seconds between clicks

def toggle_clicking(): 
    global clicking 
    clicking = not clicking 

def increase_speed(): 
    global click_delay 
    click_delay = max(0.01, click_delay - 0.01) 
    print(f"Click speed increased: {click_delay:.2f}s per click") 

def decrease_speed():
    global click_delay 
    click_delay += 0.01
    print(f"Click speed decreased: {click_delay:.2f}s per click") 

keyboard.add_hotkey("up", increase_speed)
keyboard.add_hotkey("down", decrease_speed)
keyboard.add_hotkey("shift+z", toggle_clicking)

print("Press Shift+Z to toggle clicking. Press Esc to exit.")

while True: 
    if clicking != last_state: 
        last_state = clicking
    if clicking: 
        pyautogui.mouseDown() 
        pyautogui.mouseUp()
        time.sleep(click_delay)
    if keyboard.is_pressed("esc"): 
        print("Exiting...") 
        break 