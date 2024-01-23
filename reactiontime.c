//reactiontime.c
//by Timothy Garber

//This program attempts to beat the humanbenchmark.com reaction test. On my PC, it was basically just as fast as python, but I like it more because C.

#include <windows.h>
#include <stdio.h>
#include <signal.h>

#define GREEN_COLOR RGB(75, 219, 106)

int terminated = 0;

void sigint_handler(int signo) {
    if (signo == SIGINT) {
        printf("\nProgram terminated by user.\n");
        terminated = 1;
    }
}

void click_on_green() {
    printf("Press Ctrl+C to exit the program.\n");

    signal(SIGINT, sigint_handler);

    while (!terminated) {
        POINT cursorPos;
        GetCursorPos(&cursorPos);

        HDC hdc = GetDC(NULL);
        COLORREF color = GetPixel(hdc, cursorPos.x, cursorPos.y);
        ReleaseDC(NULL, hdc);

        // Check if the color is green (adjust RGB values based on your specific green shade)
        if (color == GREEN_COLOR) {
            // Click if the color is green
            mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);
            mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0);
            printf("Clicked at %d, %d\n", cursorPos.x, cursorPos.y);
        }

        // Pause to avoid high CPU usage
        //Sleep(100);
    }
}

int main() {
    click_on_green();
    return 0;
}
