import sys
import math
import numpy as np
import cv2
q = []
# параметры цветового фильтра
hsv_min = np.array([12, 90, 185])
hsv_max = np.array([16, 255, 255])

k = 0
EPS = 33
src = cv2.imread('photos/orange_1.jpg', cv2.IMREAD_UNCHANGED)

scale_percent = 20
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

dsize = (width, height)

img = cv2.resize(src, dsize, interpolation=cv2.INTER_AREA)
hsv = cv2.cvtColor( img, cv2.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
thresh = cv2.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр


    # ищем контуры и складируем их в переменную contours
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # отображаем контуры поверх изображения

cv2.drawContours( img, contours, -1, (255,0,0), 3, cv2.LINE_AA, hierarchy, 1 )
cv2.imshow('contours', img) # выводим итоговое изображение в окно
cv2.waitKey(0)
for i in range(len(contours)):
    #print(cv.contourArea(contours[i]))
    if cv2.contourArea(contours[i]) > 100:

        print('Ученик, дневной пансион')
        break

q = []
# параметры цветового фильтра
hsv_min = np.array([3, 13, 120])
hsv_max = np.array([12, 57, 215])

k = 0
EPS = 33
src = cv2.imread('photos/white_0.jpg', cv2.IMREAD_UNCHANGED)

scale_percent = 20
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

dsize = (width, height)

img = cv2.resize(src, dsize, interpolation=cv2.INTER_AREA)
hsv = cv2.cvtColor( img, cv2.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
thresh = cv2.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр


    # ищем контуры и складируем их в переменную contours
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # отображаем контуры поверх изображения

cv2.drawContours( img, contours, -1, (255,0,0), 3, cv2.LINE_AA, hierarchy, 1 )
cv2.imshow('contours', img) # выводим итоговое изображение в окно
cv2.waitKey(0)
for i in range(len(contours)):
    #print(cv.contourArea(contours[i]))
    if cv2.contourArea(contours[i]) > 300:

        print('Учитель')
        break

q = []
# параметры цветового фильтра
hsv_min = np.array([100, 100, 0])
hsv_max = np.array([110, 175, 255])

k = 0
EPS = 33
src = cv2.imread('photos/blue_0.jpg', cv2.IMREAD_UNCHANGED)

scale_percent = 20
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

dsize = (width, height)

img = cv2.resize(src, dsize, interpolation=cv2.INTER_AREA)
hsv = cv2.cvtColor( img, cv2.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
thresh = cv2.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр


    # ищем контуры и складируем их в переменную contours
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # отображаем контуры поверх изображения

cv2.drawContours( img, contours, -1, (255,0,0), 3, cv2.LINE_AA, hierarchy, 1 )
cv2.imshow('contours', img) # выводим итоговое изображение в окно
cv2.waitKey(0)
for i in range(len(contours)):
    #print(cv.contourArea(contours[i]))
    if cv2.contourArea(contours[i]) > 100:

        print('Ученик, недельный пансион')
        break

q = []
# параметры цветового фильтра
hsv_min = np.array([116, 40, 70])
hsv_max = np.array([141, 255, 131])

k = 0
EPS = 33
src = cv2.imread('photos/purple_simple_1.jpg', cv2.IMREAD_UNCHANGED)

scale_percent = 20
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

dsize = (width, height)

img = cv2.resize(src, dsize, interpolation=cv2.INTER_AREA)
hsv = cv2.cvtColor( img, cv2.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
thresh = cv2.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр


    # ищем контуры и складируем их в переменную contours
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # отображаем контуры поверх изображения

cv2.drawContours( img, contours, -1, (255,0,0), 3, cv2.LINE_AA, hierarchy, 1 )
cv2.imshow('contours', img) # выводим итоговое изображение в окно
cv2.waitKey(0)
for i in range(len(contours)):
    #print(cv.contourArea(contours[i]))
    if cv2.contourArea(contours[i]) > 100:

        print('Ученик, полный пансион')
        break

