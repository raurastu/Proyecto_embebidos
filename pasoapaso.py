#include <math.h>
#define PI 3.141592
import RPi.GPIO as GPIO
from time import sleep

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
