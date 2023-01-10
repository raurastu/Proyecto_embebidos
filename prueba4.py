import cv2
import time
import numpy as np
import RPi.GPIO as GPIO
from time import sleep

num = 1
cap = cv2.VideoCapture(0)
colores = input("Ingrese un color (Rojo,Azul,Amarillo): ")


while True:
    ret,img = cap.read()
    cv2.imshow('Frame', img)
    if cv2.waitKey(1) & 0xFF == ord('c'):
            cv2.imwrite('/home/pi/Pictures/'+str(num)+'.jpg',img)
            print('Capture '+str(num)+' Listo!')
            num = num + 1
    if num==2:
            break
cap.release()
cv2.destroyAllWindows()

# if colores=="Azul":
#     colorbajo = np.array([100,100,20],np.uint8) #azulbajo
#     coloralto = np.array([125,255,255],np.uint8) #azulalto
# elif colores=="Amarillo":
#     colorbajo = np.array([15,100,20],np.uint8) #amarillobajo
#     coloralto = np.array([45,255,255],np.uint8) #amarilloalto
# elif colores=="Rojo":
#     colorbajo = np.array([175,100,20],np.uint8) #rojobajo
#     coloralto = np.array([179,255,255],np.uint8) #rojoalto
# 
# recorrido = 0

if colores=="Azul":
    azulbajo = np.array([100,100,20],np.uint8) #azulbajo
    azulalto = np.array([125,255,255],np.uint8) #azulalto

    im = cv2.imread('/home/pi/Pictures/1.jpg')
    frameHSV = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV,azulbajo,azulalto)
    contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contornos, -1, (255,0,0), 3)
    for c in contornos:
      area = cv2.contourArea(c)
      if area > 50:
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

    xdig = xfinal
    ydig = height-yfinal
    print(xdig)
    print(ydig)
    yanalog = (ydig*22.5)/height
    xanalog = (xdig*30)/width
    print(yanalog)
    print(xanalog)
    xanalogf = abs(15-xanalog)
    yanalogf = yanalog
    print("y",yanalogf)
    print("x",xanalogf)
    # Sacamos Angulo y recorrido
    angulo = (np.arctan(yanalogf/xanalogf))*180/3.141592653589793
    if(xanalog>15):
        angulofinal = angulo
    else:
        angulofinal = 180-angulo
    recorrido = np.sqrt((xanalogf*2)+(yanalogf*2))
    print(angulo)
    print("El RECORRIDO POR EL MOTOR DE PASO ES", recorrido)
    print("El ANGULO FINAL ES", angulofinal)
    ciclo = round((angulofinal/18)+2.5,2)
    print(ciclo)
    ciclo2 = 9
    recorrido2 = 22.36-recorrido
    
elif colores=="Amarillo":
    amarillobajo = np.array([15,100,20],np.uint8) #amarillobajo
    amarilloalto = np.array([45,255,255],np.uint8) #amarilloalto

    im = cv2.imread('/home/pi/Pictures/1.jpg')
    frameHSV = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV,amarillobajo,amarilloalto)
    contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contornos, -1, (255,0,0), 3)
    for c in contornos:
      area = cv2.contourArea(c)
      if area > 50:
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

    xdig = xfinal
    ydig = height-yfinal
    print(xdig)
    print(ydig)
    yanalog = (ydig*22.5)/height
    xanalog = (xdig*30)/width
    print(yanalog)
    print(xanalog)
    xanalogf = abs(15-xanalog)
    yanalogf = yanalog
    print("y",yanalogf)
    print("x",xanalogf)
    # Sacamos Angulo y recorrido
    angulo = (np.arctan(yanalogf/xanalogf))*180/3.141592653589793
    if(xanalog>15):
        angulofinal = angulo
    else:
        angulofinal = 180-angulo
    recorrido = np.sqrt((xanalogf*2)+(yanalogf*2))
    print(angulo)
    print("El RECORRIDO POR EL MOTOR DE PASO ES", recorrido)
    print("El ANGULO FINAL ES", angulofinal)
    ciclo = round((angulofinal/18)+2.5,2)
    print(ciclo)
    ciclo2 = 7.5
    recorrido2 = 20-recorrido


elif colores=="Rojo":
    rojobajo = np.array([175,100,20],np.uint8) #rojobajo
    rojoalto = np.array([179,255,255],np.uint8) #rojoalto
    
    im = cv2.imread('/home/pi/Pictures/1.jpg')
    frameHSV = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV,rojobajo,rojoalto)
    contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contornos, -1, (255,0,0), 3)
    for c in contornos:
      area = cv2.contourArea(c)
      if area > 50:
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

    xdig = xfinal
    ydig = height-yfinal
    print(xdig)
    print(ydig)
    yanalog = (ydig*22.5)/height
    xanalog = (xdig*30)/width
    print(yanalog)
    print(xanalog)
    xanalogf = abs(15-xanalog)
    yanalogf = yanalog
    print("y",yanalogf)
    print("x",xanalogf)
    # Sacamos Angulo y recorrido
    angulo = (np.arctan(yanalogf/xanalogf))*180/3.141592653589793
    if(xanalog>15):
        angulofinal = angulo
    else:
        angulofinal = 180-angulo
    recorrido = np.sqrt((xanalogf*2)+(yanalogf*2))
    print(angulo)
    print("El RECORRIDO POR EL MOTOR DE PASO ES", recorrido)
    print("El ANGULO FINAL ES", angulofinal)
    ciclo = round((angulofinal/18)+2.5,2)
    print(ciclo)
    ciclo2 = 6
    recorrido2 = 22.36-recorrido

led_pin=40
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin,GPIO.OUT)
pwm_led=GPIO.PWM(led_pin,50)
pwm_led.start(7.5)
pwm_led.ChangeDutyCycle(ciclo)
print("el ciclo es: ",ciclo)




demora=1/1000
cont=0
i=1
PI=3.141592653589793
In1=11
In2=13
In3=15
In4=16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(In1,GPIO.OUT)
GPIO.setup(In2,GPIO.OUT)
GPIO.setup(In3,GPIO.OUT)
GPIO.setup(In4,GPIO.OUT)

def desplazar_stepper(dist,radio,sentido):
  perimetro=2*PI*radio
  angle=360*dist/perimetro
  steps=4096*angle/360
  cont=0;
  if(sentido==1):
      i=1
      while(cont<=steps):
        if(i<=8):
          bobinas(i)
          sleep(demora)
          i+=1
          cont+=1
        else:
          i=1
          bobinas(i)
          sleep(demora)
          i+=1
          cont+=1
  else:
      i=8
      while(cont<=steps):
        if(i>=1):
          bobinas(i)
          sleep(demora)
          i-=1
          cont+=1
        else:
          i=8
          bobinas(i)
          sleep(demora)
          i-=1
          cont+=1    
  GPIO.output(In1,0)
  GPIO.output(In2,0)
  GPIO.output(In3,0)
  GPIO.output(In4,0)
  
  
  
# def Encerar():
#     i=1
#     while(1):
#         if(i<=8):
#           bobinas(i)
#           sleep(demora)
#           i+=1
#           cont+=1
#         else:
#           i=1
#           bobinas(i)
#           sleep(demora)
#           i+=1
#           cont+=1
#       if(carrera.lectura):
#           break()   

def bobinas(n):

    if(n==1):
      GPIO.output(In1,1)
      GPIO.output(In2,0)
      GPIO.output(In3,0)
      GPIO.output(In4,0)
      
    elif(n==2):
      GPIO.output(In1,1)
      GPIO.output(In2,1)
      GPIO.output(In3,0)
      GPIO.output(In4,0)
      
    elif(n==3):
      GPIO.output(In1,0)
      GPIO.output(In2,1)
      GPIO.output(In3,0)
      GPIO.output(In4,0)
      
    elif(n==4):
      GPIO.output(In1,0)
      GPIO.output(In2,1)
      GPIO.output(In3,1)
      GPIO.output(In4,0)
      
    elif(n==5):
      GPIO.output(In1,0)
      GPIO.output(In2,0)
      GPIO.output(In3,1)
      GPIO.output(In4,0)
      
    elif(n==6):
      GPIO.output(In1,0)
      GPIO.output(In2,0)
      GPIO.output(In3,1)
      GPIO.output(In4,1)
      
    elif(n==7):
      GPIO.output(In1,0)
      GPIO.output(In2,0)
      GPIO.output(In3,0)
      GPIO.output(In4,1)
      
    elif(n==8):
      GPIO.output(In1,1)
      GPIO.output(In2,0)
      GPIO.output(In3,0)
      GPIO.output(In4,1)
      
desplazar_stepper(recorrido,0.64,1)
# sleep(2)
# led=39
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(led,GPIO.OUT)
# GPIO.output(led.GPIO.HIGH)
pwm_led.ChangeDutyCycle(ciclo2)
sleep(2)
desplazar_stepper(recorrido2,0.64,1)
# GPIO.output(led.GPIO.LOW)
