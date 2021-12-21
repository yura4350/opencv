import sys
import math
import numpy as np
import cv2 as cv
q = []
# параметры цветового фильтра
hsv_min = np.array([11, 100, 20])
hsv_max = np.array([12, 255, 255])

k = 0
EPS = 33





src = cv.imread('orange_0.jpg', cv.IMREAD_UNCHANGED)

scale_percent = 20
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

dsize = (width, height)

img = cv.resize(src, dsize, interpolation=cv.INTER_AREA)


print(img.shape)



hsv = cv.cvtColor( img, cv.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
thresh = cv.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр


    # ищем контуры и складируем их в переменную contours
contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # отображаем контуры поверх изображения

cv.drawContours( img, contours, -1, (255,0,0), 3, cv.LINE_AA, hierarchy, 1 )
cv.imshow('contours', img) # выводим итоговое изображение в окно
for i in range(len(contours)):
    #print(cv.contourArea(contours[i]))
    if cv.contourArea(contours[i]) > 1000:

        print('Ученик, дневной пансион')



cv.waitKey(0)

