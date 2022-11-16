import cv2
import pyscreenshot as ImageGrab
import Finder as f
import pyautogui
import keyboard
import time

tesseract_path = r"C:\Users\Alex\AppData\Local\Tesseract-OCR\tesseract.exe"
root = r"images"

def get_mousepos():
    while(True):
        if keyboard.is_pressed('q'):
            mouse1 = pyautogui.position()
            time.sleep(1)
            mouse2 = pyautogui.position()
            return (mouse1, mouse2)


<<<<<<< Updated upstream
print("start")
=======

>>>>>>> Stashed changes
while(True):
    (pos1, pos2) = get_mousepos()
    im = ImageGrab.grab(bbox=(pos1[0], pos1[1], pos2[0], pos2[1]))
    im.save(root + r"\temp.png")
<<<<<<< Updated upstream
    imread =  cv2.imread(root + r"\temp.png")
    imread = f.filter_pixels(imread, 255, 255, 255)

    s = f.read_text(imread)
    #s = f.text_to_Int(s)
    print(s)
    print("a")

    
=======
    im.show()

    imread =  cv2.imread(root + r"\temp.png")
    print(f.read_text())
>>>>>>> Stashed changes
