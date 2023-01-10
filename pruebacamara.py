# import cv2
# import numpy as np
# 
# 
# cap= cv2.VideoCapture(0)
# 
# while True:
# 
#     _, frame = cap.read()
#     hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     
#     #RED
#     low_red = np.array([161,155,84])
#     high_red = np.array([179,255,255])
#     red_mask = cv2.inRange(hsv_frame, low_red, high_red)
#     print(red_mask)
#     contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
#     print(contours)
#     
#     for cnt in contours:
#         (x, y, w, h) = cv2.boundingRect(cnt)
#     
#     
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)
#         break
#     
#     
#     cv2.imshow("Frame",frame)
#     cv2.imshow("mask",red_mask) 
#     
#     
#     key = cv2.waitKey(1)
#     
#     if key ==27:
#         break
#     
# cap.release()
# cv2.destroyAllWindows()
# 
# 
# import cv2
# import numpy as np
# import math
# 
# dx=[0,0,1,1,-1,-1]
# dy=[1,-1,1,-1,1,-1]
# visited={}
# def dfs(x, y):
#     visited[(x,y)]=2
#     i=0
#     while i<6:
#         new_x=x+dx[i]
#         new_y=y+dy[i]
#         if(not((new_x,new_y)in visited)):
#             i+=1
#             continue
#         if(visited[(new_x,new_y)]==2):
#             i+=1
#             continue 
#         dfs(new_x,new_y)
#         i+=1
# 
import cv2
import numpy as np

azulBajo = np.array([100,100,20],np.uint8)
azulAlto = np.array([125,255,255],np.uint8)

im = cv2.imread('/home/pi/Pictures/3.jpg')
frameHSV = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(frameHSV,azulBajo,azulAlto)
contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(frame, contornos, -1, (255,0,0), 3)
for c in contornos:
  area = cv2.contourArea(c)
  if area > 3000:
    M = cv2.moments(c)
    if (M["m00"]==0): M["m00"]=1
    x = int(M["m10"]/M["m00"])
    y = int(M['m01']/M['m00'])
    print(x)
    print(y)
    cv2.circle(im, (x,y), 7, (0,255,0), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(im, '{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)
    nuevoContorno = cv2.convexHull(c)
    cv2.drawContours(im, [nuevoContorno], 0, (255,0,0), 3)


    height, width = im.shape[:2] 
      
    print("The height of the image is: ", height) 
    print("The width of the image is: ", width) 

    xfinal = x

    yfinal = y

    xdig = width-xfinal
    ydig = height-yfinal
    print(xdig)
    print(ydig)
    yanalog = (ydig*15)/height
    xanalog = (xdig*15)/width
    print(yanalog)
    print(xanalog)
    xanalogf = abs(7.5-xanalog)
    yanalogf = yanalog
    print("y",yanalogf)
    print("x",xanalogf)
    # Sacamos Angulo y recorrido
    angulo = (np.arctan(yanalogf/xanalogf))*180/3.141592653589793
    if(xanalog>7.5):
        angulofinal = angulo
    else:
        angulofinal = 180-angulo
    recorrido = np.sqrt((xanalogf*2)+(yanalogf*2))
    print(angulo)
    print("El RECORRIDO POR EL MOTOR DE PASO ES", recorrido)
    print("El ANGULO FINAL ES", angulofinal)
    ciclo = round((angulofinal/18)+2.5,2)
    print(ciclo)

print(ciclo)
import RPi.GPIO as GPIO
from time import sleep

led_pin=40
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin,GPIO.OUT)
pwm_led=GPIO.PWM(led_pin,50)
pwm_led.start(7.5)

pwm_led.ChangeDutyCycle(ciclo)