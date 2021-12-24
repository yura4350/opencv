print('Введите название файла')
import numpy as np
import cv2

#В этих двух строчках считываем изображение
fn = 'photos/' + input()
src = cv2.imread(fn, cv2.IMREAD_UNCHANGED)

#Затем выполняем изменение размеров изображения до рассматриваемых, для которых подобрана площадь
scale_percent = 800 / src.shape[1] * 100 #По этой формуле вычисляем, сколько процентов от размера должна составлять наша картинка
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

dsize = (width, height)

img = cv2.resize(src, dsize, interpolation=cv2.INTER_AREA)

#Ищем бейджик недельного пансиона

# параметры цветового фильтра
hsv_min = np.array([100, 100, 0])
hsv_max = np.array([110, 175, 255])



hsv = cv2.cvtColor( img, cv2.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
thresh = cv2.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр


# ищем контуры и складируем их в переменную contours
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Ищем контуры нужной нам площади и цвета
for i in range(len(contours)):
    if cv2.contourArea(contours[i]) > 300:

        print('Ученик, недельный пансион') #Если контур соответствует значениям площади и цвета - тогда искомый бейджик - недельного пансиона, а значит человек на фотографии - ученик недельного пансиона
        exit(0) #На картинке по условию максимум 1 беджик, значит мы нашли пансион - недельный.
        break #Если нет - проверяем следующий пансион - полный

#Ищем бейджик полного пансиона

# параметры цветового фильтра
hsv_min = np.array([116, 40, 70])
hsv_max = np.array([141, 255, 131])



hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
thresh = cv2.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр


# ищем контуры и складируем их в переменную contours
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):

    if cv2.contourArea(contours[i]) > 300:

        print('Ученик, полный пансион') #Если контур соответствует значениям площади и цвета - тогда искомый бейджик - полного пансиона, а значит человек на фотографии - ученик полного пансиона
        exit(0) #На картинке по условию максимум 1 беджик, значит мы нашли пансион - полный.
        break #Если нет - проверяем следующий пансион - дневной

#Ищем бейджик дневного пансиона

# параметры цветового фильтра
hsv_min = np.array([12, 90, 185])
hsv_max = np.array([16, 255, 255])


hsv = cv2.cvtColor( img, cv2.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
thresh = cv2.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр


    # ищем контуры и складируем их в переменную contours
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    #print(cv.contourArea(contours[i]))
    if cv2.contourArea(contours[i]) > 300:

        print('Ученик, дневной пансион') #Если контур соответствует значениям площади и цвета - тогда искомый бейджик - дневного пансиона, а значит человек на фотографии - ученик дневного пансиона
        exit(0)  #На картинке по условию максимум 1 беджик, значит мы нашли пансион - дневной.
        break #Если нет - проверяем, учительский ли бейджик

#Ищем учительский бейджик

# параметры цветового фильтра
hsv_min = np.array([3, 13, 120])
hsv_max = np.array([12, 57, 205])


hsv = cv2.cvtColor( img, cv2.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
thresh = cv2.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр


    # ищем контуры и складируем их в переменную contours
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    #print(cv.contourArea(contours[i]))
    if cv2.contourArea(contours[i]) > 300:

        print('Учитель') #Если контур соответствует значениям площади и цвета - тогда искомый бейджик - учительский, а значит человек на фотографии - учитель
        exit(0) #На картинке по условию максимум 1 беджик, значит на картинке учитель.
        break #Если нет - значит владелец бейджика не принадлежит ни к одному из этих пансионов, его невозможно опознать
print('Неопознанный объект') #На фотографии нет искомых бейджиков
