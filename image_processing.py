import cv2
img=cv2.imread('download.jpg')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blue=cv2.cvtColor(img,cv2.COLOR_BGR2RGBA)
while True:
    cv2.imshow('Shahrukh',img)
    cv2.waitKey(100)
    cv2.imshow('Shahrukh',img_gray)
    cv2.waitKey(100)
    cv2.imshow('Shahrukh',img_blue)
    cv2.waitKey(100)

