#reactiontime.py
#by Timothy Garber

#This program attempts to beat the humanbenchmark.com reaction test. On my Macbook, it was fairly slow. More testing needed on a higher refresh rate screen.

import pyautogui
import time

def click_on_green():
    try:
        while True:
            # Get the pixel color at the current cursor position
            x, y = pyautogui.position()
            color = pyautogui.pixel(x, y)

            # Check if the color is green (you might need to adjust the values based on your specific green shade)
            if color == (60, 215, 92):
                # Click if the color is green
                pyautogui.click(x, y)
                print("Clicked at", x, y)

            # Pause to avoid high CPU usage - doesn't seem to do any better on or off
            #time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    click_on_green()
