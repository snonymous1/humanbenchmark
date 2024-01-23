#aimassist.py
#By Timothy Garber

#This is used to help beat humanbenchmark.com's Aim Trainer.
#You will need to adjust your search area for your screen.

#It runs... Ok. It's not God level but that also might be due to my MacBook. More testing is needed.

import pyautogui
import time
from PIL import Image, ImageDraw

def find_white_pixel(x, y, width, height, tolerance=10):
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    for i in range(width):
        for j in range(height):
            pixel_color = screenshot.getpixel((i, j))
            # Allow some tolerance in the color matching
            if all(abs(channel - 255) <= tolerance for channel in pixel_color):
                return True, (x + i, y + j)
    return False, None

def draw_rectangle(x, y, width, height):
    screenshot = pyautogui.screenshot()
    draw = ImageDraw.Draw(screenshot)
    draw.rectangle([x, y, x + width, y + height], outline="red", width=2)
    #screenshot.show()

# Wait for 5 seconds before starting
time.sleep(5)

# Click at (700, 400) before starting the loop
pyautogui.click(700, 400)

# Specify the new area on the screen to search for a white pixel
area_x = 300
area_y = 200
area_width = 900
area_height = 600

# Draw a box around the search area
draw_rectangle(area_x, area_y, area_width, area_height)

# Loop until 30 white pixels are found
click_count = 0
while click_count < 30:
    found, coordinates = find_white_pixel(area_x, area_y, area_width, area_height)
    if found:
        print(f"White pixel found at coordinates: {coordinates}")
        
        # Add a small adjustment to the coordinates before clicking
        adjusted_x = coordinates[0] + 10  # Adjust as needed
        adjusted_y = coordinates[1] + 10  # Adjust as needed
        pyautogui.click(adjusted_x, adjusted_y)
        print("Clicked on the white pixel location.")
        
        # Increment the click count
        click_count += 1
    else:
        print("No white pixel found in the specified area. Waiting for one to appear.")

# Program finished
print("Program finished.")
