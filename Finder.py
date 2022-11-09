import cv2
import numpy as np
import pytesseract
import pyautogui
import ImageManager

def find_image(base, obj, threshold):
    result = cv2.matchTemplate(base,obj,cv2.TM_CCOEFF_NORMED)
    w = obj.shape[1]
    h = obj.shape[0]

    yLoc, xLoc = np.where(result >= threshold)

    rectangles = []
    for (x, y) in zip(xLoc, yLoc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])

    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

    #print(len(rectangles))
    return rectangles

def read_text(img):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\philipp\AppData\Local\Tesseract-OCR\tesseract.exe"
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    noise =cv2.medianBlur(gray,3)
    thresh = cv2.threshold(noise, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] 
    config = ('-l eng — oem 1 — psm 3')
    text = pytesseract.image_to_string(thresh, config=config)
    return text

def text_to_Int(text):
    result = 0
    n = 0
    for i in range(len(text)):
        s = text[len(text)-i-1]
        if(s.isnumeric()):
            result = result + int(s) * 10**n
            n = n + 1
        elif(s == " "): 
            pass
        elif(s == "S"):
            result = result + 5 * 10**n
            n = n + 1
        else:
            n = n + 1
    return result / 10        
          

