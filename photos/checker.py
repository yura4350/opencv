import cv2
src = cv2.imread('orange_0.jpg', cv2.IMREAD_UNCHANGED)

scale_percent = 20
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

dsize = (width, height)

output = cv2.resize(src, dsize, interpolation=cv2.INTER_AREA)
cv2.imshow('Image', output)
cv2.waitKey(0)