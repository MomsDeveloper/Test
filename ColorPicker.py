import cv2
import numpy as np


def empty(a):
    pass
path = 'graygirl.jpg'
cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars',640,240)
cv2.createTrackbar("Hue Min",'TrackBars',0,179,empty)
cv2.createTrackbar("Hue Max",'TrackBars',179,179,empty)
cv2.createTrackbar("Sat Min",'TrackBars',0,255,empty)
cv2.createTrackbar("Sat Max",'TrackBars',255,255,empty) 
cv2.createTrackbar("Val Min",'TrackBars',0,255,empty)
cv2.createTrackbar("Val Max",'TrackBars',65,255,empty)


frameWidth  = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

while True:
	success, img = cap.read()
	cv2.imshow('Result',img)
	# img = cv2.imread(path)
	imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	h_min = cv2.getTrackbarPos("Hue Min",'TrackBars')
	h_max = cv2.getTrackbarPos("Hue Max",'TrackBars')
	s_min = cv2.getTrackbarPos("Sat Min",'TrackBars')
	s_max = cv2.getTrackbarPos("Sat Max",'TrackBars')
	v_min = cv2.getTrackbarPos("Val Min",'TrackBars')
	v_max = cv2.getTrackbarPos("Val Max",'TrackBars')

	lower = np.array([h_min,v_min,s_min])
	upper = np.array([h_max,v_max,s_max])

	mask = cv2.inRange(imgHSV,lower,upper)
	imgResult = cv2.bitwise_and(img,img,mask=mask)

	print(h_min,h_max,s_min,s_max,v_min,v_max)
	cv2.imshow('Original',img)
	cv2.imshow('HSV',imgHSV)
	cv2.imshow('HSV_regulation', mask)
	cv2.imshow('HSV Result', imgResult)


	if cv2.waitKey(1) & 0xFF ==ord('q'):
		break

