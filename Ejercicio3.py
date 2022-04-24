

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

#definir iterador para tarjeta
iterator = pyfirmata.util.Iterator(board)
iterator.start()

#Setear pin digital que se utilizará con el potenciometro
pot = board.get_pin('a:0:i')

#Función potenciometro para capturar datos y general la intensidad para las salidas digitales 
#Intensidad de visaulizacion de Ascendente/Descendente
def poten():
    po = pot.read()
    if po is not None:
        espera = po + 0.01
        time.sleep(espera)
        led6.write(1)
        time.sleep(espera)
        led5.write(1)
        time.sleep(espera)
        led4.write(1)
        time.sleep(espera)
        led3.write(1)
        time.sleep(espera)
        led2.write(1)
        time.sleep(espera)
        led1.write(1)
        time.sleep(espera)
        led6.write(0)
        led5.write(0)
        led4.write(0)
        led3.write(0)
        led2.write(0)
        led1.write(0)
        time.sleep(espera)
        led1.write(1)
        time.sleep(espera)
        led2.write(1)
        time.sleep(espera)
        led3.write(1)
        time.sleep(espera)
        led4.write(1)
        time.sleep(espera)
        led5.write(1)
        time.sleep(espera)
        led6.write(1)
        time.sleep(espera)
        led1.write(0)
        led2.write(0)
        led3.write(0)
        led4.write(0)
        led5.write(0)
        led6.write(0)
    else:
        time.sleep(0.1)


while True:
    poten() #Ejecución infinita hasta finalizar 

