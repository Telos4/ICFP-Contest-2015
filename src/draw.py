import cv2
import numpy as np

import handlejson as hj
from data import *

def drawBoard(width, height, scale):
    width = width+1
    height = height
    w = scale
    h = scale

    img = np.zeros((height*scale, width*scale, 3), np.uint8)
    img[:,:] = (0,0,0)
    for i in range(width-1):
        for j in range(height):
            if j % 2 == 0:
                x = i*scale
                y = j*scale
            else:
                x = i*scale + w/2 # odd rows shifted to the right
                y = j*scale

            cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255), thickness=cv2.cv.CV_FILLED)
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,0))

    return img

def drawCell(img, width, height, scale):
    w = scale
    h = scale

    if height % 2 == 0:
        x = width*scale
        y = height*scale
    else:
        x = width*scale + w/2 # odd rows shifted to the right
        y = height*scale
    
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), thickness=cv2.cv.CV_FILLED)

if __name__ == '__main__':
    datas = [data0, data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16, data17, data18, data19, data20, data21, data22, data23]

    for i in range(len(datas)):
        data = datas[i]
        
        parsedData = hj.parse_to_dictionary(data)

        width = parsedData['width']
        height = parsedData['height']
        scale = 20
        filled = parsedData['filled']

        img = drawBoard(width, height, scale)

        for cell in filled:
            drawCell(img, cell['x'], cell['y'], scale)

        cv2.imwrite('Maps/map_' + str(i) + '.png', img)

        #while not (cv2.waitKey(1) & 0xFF == ord('q')):
            #cv2.imshow('test', img)
