
import pyfirmata #Librerpía de Comunicación con tarjeta Arduino
import time #Libreria de tiempo
board = pyfirmata.Arduino('/dev/cu.usbmodem2201') #Puerto al que esta conectado la tarjeta
print("*** TARJETA ARDUINO CONECTADA ***")

while True:
    #Leds del 7 al 2
    for i in list(range (7,1,-1)): #Lista del rango 7 al 1
        board.digital[i].write(1)
        time.sleep(.1)
        board.digital[i].write(0)
        time.sleep(.1)
    #Leds del 2 al 7
    for a in list(range (2,8)): #Lista del rango 2 al 8
        board.digital[a].write(1)
        time.sleep(.1)
        board.digital[a].write(0)
        time.sleep(.1)
            