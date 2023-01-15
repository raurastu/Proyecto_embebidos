import cv2
import time
import numpy as np
import RPi.GPIO as GPIO
from time import sleep
led_pin=40
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin,GPIO.OUT)
pwm_led=GPIO.PWM(led_pin,50)
pwm_led.start(7.5)
pwm_led.ChangeDutyCycle(12.5)
#pwm_led=GPIO.PWM(led_pin,0)
demora=1/1000
PI=3.141592653589793
FC_in=18
FC_out=19
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(FC_in,GPIO.IN)
GPIO.setup(FC_out,GPIO.IN)
def angulo_stepper(sentido,angle):
  In1=3
  In2=5
  In3=7
  In4=11
  steps=4096*angle/360
  print(steps)
  i=1
  cont=0
  if(sentido==-1):
      i=1
      while(cont<=steps and GPIO.input(FC_in) and GPIO.input(FC_out)):
        if(i<=8):
          bobinas2(i,motor)
          sleep(demora)
          i+=1
          cont+=1
        else:
          i=1
          bobinas2(i,motor)
          sleep(demora)
          i+=1
          cont+=1
  else:
      i=8
      while(cont<=steps and GPIO.input(FC_in) and GPIO.input(FC_out)):
        if(i>=1):
          bobinas2(i,motor)
          sleep(demora)
          i-=1
          cont+=1
        else:
          i=8
          bobinas2(i,motor)
          sleep(demora)
          i-=1
          cont+=1    
  GPIO.output(In1,0)
  GPIO.output(In2,0)
  GPIO.output(In3,0)
  GPIO.output(In4,0)

def desplazar_stepper(dist,radio,sentido,motor):
  if(motor=="grua"):
      In1=12
      In2=13
      In3=15
      In4=16
  elif(motor=="iman"):
      In1=3
      In2=5
      In3=7
      In4=11
  perimetro=2*PI*radio
  angle=360*dist/perimetro
  steps=4096*angle/360
  i=1
  cont=0
  if(sentido==-1):
      i=1
      while(cont<=steps and GPIO.input(FC_in) and GPIO.input(FC_out)):
        if(i<=8):
          bobinas(i,motor)
          sleep(demora)
          i+=1
          cont+=1
        else:
          i=1
          bobinas(i,motor)
          sleep(demora)
          i+=1
          cont+=1
  else:
      i=8
      while(cont<=steps and GPIO.input(FC_in) and GPIO.input(FC_out)):
        if(i>=1):
          bobinas(i,motor)
          sleep(demora)
          i-=1
          cont+=1
        else:
          i=8
          bobinas(i,motor)
          sleep(demora)
          i-=1
          cont+=1    
  GPIO.output(In1,0)
  GPIO.output(In2,0)
  GPIO.output(In3,0)
  GPIO.output(In4,0)
  
def bobinas2(n,motor):
    In1=29
    In2=31
    In3=33
    In4=35
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
      
def bobinas(n,motor):
    if(motor=="rotor"):
      In1=29
      In2=31
      In3=33
      In4=35
    if(motor=="grua"):
      In1=12
      In2=13
      In3=15
      In4=16
    elif(motor=="iman"):
      In1=3
      In2=5
      In3=7
      In4=11
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

def bobinas2(n,motor):
    In1=29
    In2=31
    In3=33
    In4=35
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
      
def bobinas(n,motor):
    if(motor=="rotor"):
      In1=29
      In2=31
      In3=33
      In4=35
    if(motor=="grua"):
      In1=12
      In2=13
      In3=15
      In4=16
    elif(motor=="iman"):
      In1=3
      In2=5
      In3=7
      In4=11
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
angulo_stepper(-1,180,"rotor")
#desplazar_stepper(50,0.5,1,"grua")
def capturar(cap):
    ret,img = cap.read()
    cv2.imshow('Frame', img)
    cv2.imwrite('/home/pi/Pictures/'+str(num)+'.jpg',img)
print("hola")
num = 1
print("hola2")
cap = cv2.VideoCapture(0)
print("hola3")
colores = input("Ingrese un color (Rojo,Azul,Amarillo): ")
#capturar(cap)

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
    x=-5
    y=-5
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

    if(x>0 and y>0):
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
        recorrido2 = 8-recorrido
    else:
        print("No se encontro nada")
        
elif colores=="Amarillo":
    x=-5
    y=-5
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
    
    if(x>0 and y>0):
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
        recorrido2 = 7-recorrido
    else:
        print("No se encontro nada")


elif colores=="Rojo":
    x=-5
    y=-5
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

    if(x>0 and y>0):
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
        ciclo2 = 8
        recorrido2 = 8-recorrido
    else:
        print("No se encontro nada")
led_pin=40
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin,GPIO.OUT)
if(x>0 and y>0):
    #pwm_led=GPIO.PWM(led_pin,50)
    pwm_led.start(7.5)
    pwm_led.ChangeDutyCycle(ciclo)
    angulo_stepper(-1,angulofinal,"rotor")
    print("el ciclo es: 2",ciclo)
    desplazar_stepper(recorrido,0.2,1,"grua")
    #pwm_led=GPIO.PWM(led_pin,0)
    desplazar_stepper(5,1,1,"iman")
    sleep(1)
    desplazar_stepper(5,1,-1,"iman")
    pwm_led.ChangeDutyCycle(ciclo2)
    desplazar_stepper(recorrido2,0.2,1,"grua")
    desplazar_stepper(5,1,1,"iman")
    sleep(1)
    desplazar_stepper(5,1,-1,"iman")




# sleep(2)
# led=39
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(led,GPIO.OUT)
# GPIO.output(led.GPIO.HIGH)

# GPIO.output(led.GPIO.LOW)
