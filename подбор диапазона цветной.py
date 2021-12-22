import cv2
import numpy as np

low_H = 0
low_S = 0
low_V = 0
high_H = 180
high_S = 255
high_V = 255


def thresh_trackbar(_):
    low_H = cv2.getTrackbarPos('1_low_H','HSV demo')
    low_S = cv2.getTrackbarPos('2_low_S','HSV demo')
    low_V = cv2.getTrackbarPos('3_low_V','HSV demo')
    high_H = cv2.getTrackbarPos('4_high_H','HSV demo')
    high_S = cv2.getTrackbarPos('5_high_S','HSV demo')
    high_V = cv2.getTrackbarPos('6_high_V','HSV demo')
    low = np.array([low_H, low_S, low_V])
    high = np.array([high_H, high_S, high_V])
    mask = cv2.inRange(img, low, high)
    result = image1.copy()
    result = cv2.bitwise_and(result, result, mask=mask)
    cv2.imshow('HSV demo', result)
    print(low_H, low_S, low_V, high_H, high_S, high_V)


image=cv2.imread("photos/purple_0.jpg")
image1 = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
img = image.copy()

cv2.imshow("HSV demo", img)

cv2.createTrackbar('1_low_H', 'HSV demo', 0, 180, thresh_trackbar)
cv2.createTrackbar('2_low_S', 'HSV demo', 0, 255, thresh_trackbar)
cv2.createTrackbar('3_low_V', 'HSV demo', 0, 255, thresh_trackbar)
cv2.createTrackbar('4_high_H', 'HSV demo', 0, 180, thresh_trackbar)
cv2.createTrackbar('5_high_S', 'HSV demo', 0, 255, thresh_trackbar)
cv2.createTrackbar('6_high_V', 'HSV demo', 0, 255, thresh_trackbar)


cv2.waitKey(0)