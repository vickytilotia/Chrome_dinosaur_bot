import pyautogui # pip install pyautogui
# to control GUI
from PIL import Image, ImageGrab # pip install pillow
# to take screenshot and modify image
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

"""def isCollide(data):
    # Draw the rectangle for birds
    for i in range(300, 415):
        for j in range(410, 563):
            if data[i, j] < 100:
                hit("down")
                return

    for i in range(300, 415):
        for j in range(563, 650):
            if data[i, j] < 100:
                hit("up")
                return
    return
"""
if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        image.show()
        #isCollide(data)
            
        # print(asarray(image))
        
        # Draw the rectangle for cactus
        for i in range(175, 200):
            for j in range(380, 460):
                data[i, j] = 0
        
        # Draw the rectangle for birds
        for i in range(200, 230):
                
            for j in range(300, 360):
                data[i, j] = 171

        image.show()
        break
      

