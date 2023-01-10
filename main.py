import bluetooth
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
led_pin = 11
GPIO.setup(led_pin, GPIO.OUT)
host = ""
port = 1
server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print('Socket de Bluetooth creado')
try:
server.bind((host, port))
print("Binding completo")
except:
print("Binding incompleto")
server.listen(1)
cliente, direccion = server.accept()
print("Conectado a:", direccion)
print("Cliente:", cliente)
try:
while True:
dato = cliente.recv(1024)
print(dato)
if dato == 'A':
GPIO.output(led_pin, 1)
elif data == 'B':
GPIO.output(led_pin, False)
else:
print("Solo puede enviar A o B")
except KeyboardInterrupt:
GPIO.cleanup()
client.close()
server.close()
