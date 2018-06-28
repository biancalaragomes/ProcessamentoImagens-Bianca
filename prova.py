import cv2
import queue
import numpy as np


captura = cv2.VideoCapture('video.mp4')

while (1):
    ret, frame = captura.read()
    lin, col, cor= frame.shape
    bin = np.ones((lin, col), np.uint8)
    for i in range(0, lin):
        for j in range(0, col):
            b = frame.item(i, j, 0)
            r = frame.item(i, j, 2)
            g = frame.item(i, j, 1)
            if r > 95 and g > 40 and b > 20 and abs(r - g) > 15 and r > g and r > b:
                bin.itemset(i, j, 255)
            else:
                bin.itemset(i, j, 0)

	bin = cv2.dilate(bin, mask, it=1)
    bin = cv2.erode(bin, mask, it=5)   
    cv2.imshow('frame', bin)
	mask = np.ones((3, 3), np.uint8)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

captura.release()