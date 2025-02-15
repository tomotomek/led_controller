import sys
import pyscreenshot as ImageGrab
import numpy as np
import requests
from time import sleep
import json

#API_ENDPOINT = 'http://<IP addr>:<port>'
API_ENDPOINT = sys.argv[1]
INTERVAL = 1

def averageColorOfScreen():
    image = ImageGrab.grab()
    imageMatrix = np.array(image)
    r = int(np.mean(imageMatrix[:,:,0]))
    g = int(np.mean(imageMatrix[:,:,1]))
    b = int(np.mean(imageMatrix[:,:,2]))
    print([r, g, b])
    data = {
            'RGBcolor':[r,g,b]
            } 
    r = requests.post(url = API_ENDPOINT, data = json.dumps(data))
    print('Server response: ', r.text)

if __name__ == '__main__':

  while True:
    try:
      averageColorOfScreen()
      sleep(INTERVAL)
    except:
      print('Probably server at {} is disconnected'.format(API_ENDPOINT))
      sleep(5*60)
