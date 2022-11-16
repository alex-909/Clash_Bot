import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt 
import ImageManager as im
import time

tesseract_path = r"C:\Users\Alex\AppData\Local\Tesseract-OCR\tesseract.exe"
#tesseract_path = r"C:\Users\philipp\AppData\Local\Tesseract-OCR\tesseract.exe"
#tesseract_path = r"D:\MeineDaten\Programmieren\Python\Tesseract\tesseract.exe"

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
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    noise = cv2.medianBlur(gray,3)
    thresh = cv2.threshold(noise, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] 
    config = ('-l eng — oem 1 — psm 3')
    text = pytesseract.image_to_string(thresh, config=config)
    return text

def filter_pixels(img, _r, _g, _b):
    (_h, _w) = img.shape[:2]
    for h in range(_h):
        for w in range(_w):
            (b,g,r) = img[h,w]
            if (b == _b and g == _g and r == _r):
                img[h,w] = (255,255,255)
            else:
                img[h,w] = (0,0,0)
    return img


def text_to_Int(text): # needs fixing
    pairs = [
        ("S", "5"), 
        ("s", "5"), 
        (" ", ""),
        ("I", "1"),
        ("i", "1"), 
        ("l", "1"), 
        ("o","0"),
        ("O","0"),
        ("n", "0"),
        ("(", "0"),
        (")", "0"),
        ("D", "0")
        ]
    for pair in pairs:
        text = text.replace(pair[0], pair[1])
    return int(text)
          

        