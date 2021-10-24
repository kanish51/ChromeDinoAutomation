import pyautogui
from PIL import Image, ImageGrab
import time

xi = 500
xf = 600
count = 0

def isColliding(img):
    global count
    for i in range(xi,xf):
        for j in range(650,700):
            if img[i,j] !=  img[59,165]:
                count = count + 1
                pyautogui.press('up')
                return 

    for i in range(xi,xf):
        for j in range(590,630):
            if img[i,j] !=  img[59,165]:
                count = count + 1
                pyautogui.keyDown('down')
                time.sleep(0.3)
                pyautogui.keyUp('down')
                return 

    return



if __name__ == "__main__":
    time.sleep(2)
    while True:
        if count > 10:
            count = 0
            xi = xi+5
            xf = xf+15 
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isColliding(data)
