#typingtest.py
#By Timothy Garber

#This is a program designed to beat humanbenchmark.com's typing test.
#You will likely need to adjust your reading region to make it work.

#Also, it occasionally misreads. It's not perfect, but you can just not save and rerun it until you get a good result.

import pyautogui
from PIL import Image
import pytesseract
from io import BytesIO
import time

def type_text_from_screen(x, y, width, height):
    # Capture the screen region
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    # Convert the screenshot to bytes
    screenshot_bytes = BytesIO()
    screenshot.save(screenshot_bytes, format='PNG')

    # Use pytesseract to perform OCR on the image in memory
    text = pytesseract.image_to_string(Image.open(screenshot_bytes))

    # Remove or replace return characters (newline, carriage return) with a space
    text = text.replace('\n', ' ').replace('\r', ' ')

    #for debugging purposes
    print(text)

    # Type the extracted text via keyboard key presses
    pyautogui.typewrite(text)

# Set the coordinates (x, y) and dimensions (width, height) of the screen region to capture
screen_region = (240, 380, 1000, 500)

# Wait for 5 seconds
time.sleep(5)

# Call the function with the specified screen region
type_text_from_screen(*screen_region)
