
import pyfirmata #Librerpía de Comunicación con tarjeta Arduino
import time #Libreria de tiempo
board = pyfirmata.Arduino('/dev/cu.usbmodem2201') #Puerto al que esta conectado la tarjeta
print("\n*** TARJETA ARDUINO CONECTADA ***")

#Definición de variables leds para salidas digitales
led1 = board.digital[2]
led2 = board.digital[3]
led3 = board.digital[4]
led4 = board.digital[5]
led5 = board.digital[6]
led6 = board.digital[7]

while True:
    #Primera mitad de Leds
    led1.write(1)
    led2.write(1)
    led3.write(1)
    time.sleep(1)
    led1.write(0)
    led2.write(0)
    led3.write(0)
    #Otra mitad de Leds
    led4.write(1)
    led5.write(1)
    led6.write(1)
    time.sleep(2)
    led4.write(0)
    led5.write(0)
    led6.write(0)
        