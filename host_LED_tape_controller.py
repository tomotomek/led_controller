import sys
import pyscreenshot as ImageGrab
import numpy as np
import requests
from time import sleep
from magichome import MagicHomeApi

INTERVAL = 1

def averageColorOfScreen():
    image = ImageGrab.grab()
    imageMatrix = np.array(image)
    r = int(np.mean(imageMatrix[:,:,0]))
    g = int(np.mean(imageMatrix[:,:,1]))
    b = int(np.mean(imageMatrix[:,:,2]))
    rgb = [r,g,b]
    rgb[rgb.index(min(rgb))] = int(rgb[rgb.index(min(rgb))] * 0.5) #FIEXME
    rgb[rgb.index(max(rgb))] = min(255, int(rgb[rgb.index(max(rgb))] * 1.8)) #FIEXME
    print(rgb)
    
    controller.update_device(rgb[0], rgb[1], rgb[2])


if __name__ == '__main__':
  controller = MagicHomeApi('192.168.0.27', 1)
  controller.turn_on()
  while True:
    try:
      averageColorOfScreen()
      sleep(INTERVAL)
    except:
      print('Something went wrong')
      sleep(5*60)
