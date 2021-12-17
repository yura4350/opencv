import sys
import math
import numpy as np
import cv2 as cv
q = []
# параметры цветового фильтра
hsv_min = np.array([10, 100, 20])
hsv_max = np.array([20, 255, 255])

k = 0
EPS = 33

fn = 'photos/orange_0.jpg' # путь к файлу с картинкой

img = cv.imread(fn, cv.IMREAD_UNCHANGED)
print(img.shape)
#cale_percent = 20
#width = int(img.shape[1] * scale_percent / 100)
#height = int(img.shape[0] * scale_percent / 100)
#dsize = (width, height)
#img = img.resize(img, int(img.shape[1] / 5), int(img.shape[0] / 5))


hsv = cv.cvtColor( img, cv.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
thresh = cv.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр


    # ищем контуры и складируем их в переменную contours
contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # отображаем контуры поверх изображения

cv.drawContours( img, contours, -1, (255,0,0), 3, cv.LINE_AA, hierarchy, 1 )
cv.imshow('contours', img) # выводим итоговое изображение в окно
for i in range(len(contours)):
    #print(cv.contourArea(contours[i]))
    if cv.contourArea(contours[i]) > 300:

        print('Ученик, дневной пансион')



cv.waitKey(0)

