#verbalmemory.py
#by Timothy Garber

#This program is used to beat humanbenchmark.com's Verbal Memory game.
#You will likely need to adjust the capture region and clicking locations.

import pyautogui
import time
import pytesseract

#You may need this line if you are on windows
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

def check_word_status(word, old_words):
    if word in old_words:
        return "Old word"
    else:
        old_words.append(word)
        return "New word"

def main():

    time.sleep(5) #give myself 5 seconds to set up screen

    old_words = []

    print("Press Ctrl+C to exit the program.")

    try:
        while True:
            #time.sleep(0.01)  # Adjust this sleep time based on your needs

            # Capture the screenshot within the specified coordinates
            region = (500, 350, 500, 100)
            screenshot = pyautogui.screenshot(region=region).convert("RGB")

            # Perform OCR (Optical Character Recognition) on the captured screenshot
            word_text = pytesseract.image_to_string(screenshot)

            status = check_word_status(word_text.lower(), old_words)
            print(f'This is a {status}.')

            # Perform mouse click based on status
            if status == "Old word":
                pyautogui.click(600, 480)
            elif status == "New word":
                pyautogui.click(800, 480)

    except KeyboardInterrupt:
        print("\nExiting program.")

if __name__ == "__main__":
    main()
