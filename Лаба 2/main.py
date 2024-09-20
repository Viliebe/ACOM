import cv2
import numpy as np


#Задание 1

# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     cv2.imshow('hsv_frame', hsv)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
# cap.release()
# cv2.destroyAllWindows()

# # #Задание 2

# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     maska=cv2.inRange(hsv,(0,155,155),(30,255,255))
#     onlyRed_frame = cv2.bitwise_and(frame, frame, mask = maska)
#     cv2.imshow('Фильтрация красного изображения', onlyRed_frame)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
# cap.release()
# cv2.destroyAllWindows()

#Задание 3

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    maska=cv2.inRange(hsv,(0,155,155),(30,255,255))
    kernel = np.ones((5, 5), np.uint8)
    image_opening = cv2.morphologyEx(maska, cv2.MORPH_OPEN, kernel)
    image_closing = cv2.morphologyEx(maska, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Open", image_opening)
    cv2.imshow("Close", image_closing)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()

#Задание 4-5

# cap = cv2.VideoCapture(0)
# kernel=np.ones((5,5),np.uint8)
# while True:
#     ret, frame = cap.read()
#     if not(ret):
#         break
#     HSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#     maska=cv2.inRange(HSV,(0,155,155),(30,255,255))
#     opened=cv2.morphologyEx(maska,cv2.MORPH_OPEN,kernel)
#     openmoments=cv2.moments(opened)
#     if(openmoments["m00"]!=0):
#         print(f"Площадь: {openmoments['m00']}")
#         print(f"Моменты 1 порядка: {openmoments['m01']}, {openmoments['m10']}")
#         x=int(openmoments['m10']/openmoments['m00'])
#         y=int(openmoments['m01']/openmoments['m00'])
#
#         (contours, _) = cv2.findContours(opened.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#         for countour in contours:
#             (x, y, w, h) = cv2.boundingRect(countour)
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)
#             x = int(x + w / 2)
#             y = int(y + w / 2)
#             cv2.circle(frame, (x, y), 1, (0, 0, 0), 2)
#     cv2.imshow('Обнаружение',frame)
#     if cv2.waitKey(1) & 0XFF == 27:
#         break
# cv2.destroyAllWindows()