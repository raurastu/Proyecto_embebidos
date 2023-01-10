import RPi.GPIO as GPIO
from time import sleep

led_pin=21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
pwm_led=GPIO.PWM(led_pin,50)
pwm_led.start(7.5)
# try:
#     while True:
pwm_led.ChangeDutyCycle()
#        sleep(0.5)
#        pwm_led.ChangeDutyCycle(10.5)
#        sleep(0.5)
#        pwm_led.ChangeDutyCycle(7.5)
#        sleep(0.5)
# 
# except KeyboardInterrupt:
#     pwm_led.stop()
#     GPIO.cleanup()