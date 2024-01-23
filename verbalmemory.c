#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <tesseract/baseapi.h>
#include <leptonica/allheaders.h>

void check_word_status(char *word, char **old_words, int *old_words_count) {
    for (int i = 0; i < *old_words_count; i++) {
        if (strcmp(word, old_words[i]) == 0) {
            printf("Old word\n");
            return;
        }
    }

    old_words[*old_words_count] = strdup(word);
    (*old_words_count)++;
    printf("New word\n");
}

void click_at_coordinates(int x, int y) {
    // Implement the function to simulate a mouse click at the specified coordinates
    // You can use Windows API functions like SetCursorPos and mouse_event
    // Example:
    SetCursorPos(x, y);
    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);
    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0);
}

void main_loop() {
    printf("Press Ctrl+C to exit the program.\n");

    char **old_words = NULL;
    int old_words_count = 0;

    try {
        while (1) {
            // Sleep for 5 seconds to set up screen
            sleep(5);

            // Capture the screenshot within the specified coordinates
            system("screencapture -R500,350,500,100 screenshot.png");

            // Perform OCR using Tesseract
            tesseract::TessBaseAPI *api = new tesseract::TessBaseAPI();
            api->Init(NULL, "eng", tesseract::OEM_DEFAULT);
            api->SetPageSegMode(tesseract::PSM_AUTO);

            Pix *image = pixRead("screenshot.png");
            api->SetImage(image);

            char *word_text = api->GetUTF8Text();
            pixDestroy(&image);

            check_word_status(word_text, old_words, &old_words_count);

            // Perform mouse click based on status
            if (old_words_count > 0) {
                // Adjust coordinates based on your requirements
                click_at_coordinates(600, 480);
                usleep(100000);
                click_at_coordinates(800, 480);
                usleep(100000);
            }

            delete[] word_text;
        }
    } catch (int sig) {
        printf("\nExiting program.\n");
        for (int i = 0; i < old_words_count; i++) {
            free(old_words[i]);
        }
        free(old_words);
    }
}

int main() {
    main_loop();
    return 0;
}
