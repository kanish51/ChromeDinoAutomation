import pyautogui
from PIL import Image, ImageGrab
import time

def isColliding(data):
    for i in range(505, 565):
        for j in range(605, 675):
            if data[i, j] < 100:
                pyautogui.press("up")
                return
    return

if __name__ == "__main__":
    time.sleep(2)
    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isColliding(data)

        '''for i in range(505, 575):
            for j in range(605, 675):
                data[i, j] = 0
        image.show()
        break'''
        #470 530 562 670
