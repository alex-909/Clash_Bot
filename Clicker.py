import pyautogui
import keyboard

def click(x, y):
    pyautogui.click(x, y)

def drag_top_left():
    pyautogui.moveTo(860, 440)
    pyautogui.mouseDown(button = 'left')
    pyautogui.moveTo(1260, 840, 0.5)
    pyautogui.mouseUp(button = 'left')

def drag_top_builder_menu():
    for i in range(10):
        pyautogui.moveTo(777, 270)
        pyautogui.mouseDown(button = 'left')
        pyautogui.moveTo(777, 700, 0.5)
        pyautogui.mouseUp(button = 'left')

def drag_down_builder_menu():
        pyautogui.moveTo(777, 700)
        pyautogui.mouseDown(button = 'left')
        pyautogui.moveTo(777, 250, 0.5)
        pyautogui.mouseUp(button = 'left')
