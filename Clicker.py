import pyautogui
import keyboard

def click(x, y):
    pyautogui.click(x, y)

def drag_top_left():
    pyautogui.moveTo(860, 440)
    pyautogui.mouseDown(button = 'left')
    pyautogui.moveTo(1260, 840, 0.5)
    pyautogui.mouseUp(button = 'left')
