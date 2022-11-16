import pyautogui
import time

lastPress = 0

def click(rects):
    if(len(rects)):
        pyautogui.click(rects[0][0], rects[0][1])
        refresh_time()
    else:
        print("rects is empty at CLicker.py!")

def click_xy(x, y):
    pyautogui.click(x,y)
    refresh_time()


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

def get_time():
    return time.time()

def last_press_time():
    tmp = get_time()
    return tmp - lastPress

def refresh_time():
    lastPress = get_time()
    
