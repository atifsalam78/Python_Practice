import pyautogui
from PIL import Image, ImageGrab
import time
# import numpy as np

def hit(key):
    pyautogui.keyDown(key)
    

def isCollide(data):
    for i in range(490, 510):
        for j in range(290, 300):
            if data[i,j] < 100:
                return True
    return False
    

if __name__=="__main__":
    print("Hey... Dino game is about to begin in once second")
    time.sleep(1)
    hit("up")

    while True:
        image1 = ImageGrab.grab().convert("L")
        data = image1.load()
        if isCollide(data):
            hit("up")
        # # print(np.ascontiguousarray(image))
    # for i in range(490, 510):
    #     for j in range(290, 300):
    #         data[i,j] = 0
    # image1.show()

