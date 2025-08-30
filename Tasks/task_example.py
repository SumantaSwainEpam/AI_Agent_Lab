import pyautogui
import time

def open_notepad_and_type():
    """
    Example task: Open Notepad and type a message.
    """
    pyautogui.hotkey("win", "r")
    time.sleep(1)
    pyautogui.typewrite("notepad\n", 0.1)
    time.sleep(1)
    pyautogui.typewrite("Automation works with Gemini AI!", 0.1)
