import pyautogui # pip install pyautogui
# to control GUI
from PIL import Image, ImageGrab # pip install pillow
# to take screenshot and modify image
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # Draw the rectangle for birds
    """for i in range(230, 250):
        for j in range(300, 380):
            if data[i, j] > 100:
                hit("down")
                return
    
    """
    # Draw rectangle for cactus
    for i in range(400, 430):
        for j in range(380, 455):
            if data[i, j] > 100:
                if data[i,j] < 220:
                    hit("up")
                    return
    
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        #image.show()
        isCollide(data)
            
        # print(asarray(image))
        
        """# Draw the rectangle for cactus
        for i in range(250, 260):
            for j in range(380, 455):
                data[i, j] = 0
                
        
        # Draw the rectangle for birds
        for i in range(230, 240):
                
            for j in range(300, 360):
                data[i, j] = 220

        image.show()
        break
        """
      

