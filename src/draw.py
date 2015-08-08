#import cv2
import numpy as np
import os

import handlejson as hj
from data import *
import data_structures as ds

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

def drawCell(img, color, width, height, scale):
    w = scale
    h = scale

    if height % 2 == 0:
        x = width*scale
        y = height*scale
    else:
        x = width*scale + w/2 # odd rows shifted to the right
        y = height*scale
    
    cv2.rectangle(img, (x,y), (x+w,y+h), color, thickness=cv2.cv.CV_FILLED)

def drawPivot(img, color, width, height, scale):
    w = scale
    h = scale

    if height % 2 == 0:
        x = width*scale
        y = height*scale
    else:
        x = width*scale + w/2 # odd rows shifted to the right
        y = height*scale

    cv2.rectangle(img, (x+w/3,y+h/3), (x+w-w/3,y+h-h/3), color, thickness=cv2.cv.CV_FILLED)

"""
if __name__ == '__main__':
    parsedData = hj.parse_to_dictionary(data20)
    units = parsedData['units']
    filled = parsedData['filled']
    width = parsedData['width']
    height = parsedData['height']
    scale = 20

    img = drawBoard(width, height, scale)

    unit = ds.Unit(units[3])
    unit = unit.moveToSpawnPosition(width)
    unit = unit.move('SW')
    unit = unit.move('SE')
    unit = unit.move('SW')

    for cell in unit.members:
        drawCell(img, (0,255,0), cell.x, cell.y, scale) 

    unit = unit.move('RCC')
    
    for cell in filled:
        drawCell(img, (0,0,255), cell['x'], cell['y'], scale)

    for cell in unit.members:
        drawCell(img, (255,0,0), cell.x, cell.y, scale)

    drawPivot(img, (0,0,0), unit.pivot.x, unit.pivot.y, scale)
    
    cv2.imwrite('unit.png', img)
"""
"""
    datas = [data0, data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16, data17, data18, data19, data20, data21, data22, data23]

    for i in range(len(datas)):
        data = datas[i]
        
        parsedData = hj.parse_to_dictionary(data)

        width = parsedData['width']
        height = parsedData['height']
        scale = 20
        filled = parsedData['filled']
        units = parsedData['units']

        if not os.path.exists('Maps'):
            os.makedirs('Maps')

        directory = 'Maps/Map_' + str(i)
        if not os.path.exists(directory):
            os.makedirs(directory)

        for j in range(len(units)):
            img = drawBoard(width, height, scale)
            for cell in units[j]['members']:
                drawCell(img, (255,0,0), cell['x'], cell['y'], scale)

            pivot = units[j]['pivot']
            drawPivot(img, (0,255,0), pivot['x'], pivot['y'], scale)

            cv2.imwrite(directory + '/unit_' + str(j) + '.png', img)


        img = drawBoard(width, height, scale)

        for cell in filled:
            drawCell(img, (0,0,255), cell['x'], cell['y'], scale)

        cv2.imwrite(directory + '/map_' + str(i) + '.png', img)

        #while not (cv2.waitKey(1) & 0xFF == ord('q')):
            #cv2.imshow('test', img)
"""
