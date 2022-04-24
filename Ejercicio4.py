
from cgitb import reset
import colorama
from colorama import Fore
from colorama import Style
import pyfirmata #Librerpía de Comunicación con tarjeta Arduino
import time #Libreria de tiempo
board = pyfirmata.Arduino('/dev/cu.usbmodem2201') #Puerto al que esta conectado la tarjeta
print("\n*** TARJETA ARDUINO CONECTADA ***\n")

e = "Encendido;  "
a = " Apagado;    "
g = "            "
f = "            "
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


def poten():
    po = pot.read()
    if po is not None:
        espera = po + 0.01
        time.sleep(espera)
        led6.write(1)
        print (led6,(Fore.RED+Style.BRIGHT + e) + Style.RESET_ALL, g,f, g,f, g,f, g,f, g,f)
        time.sleep(espera)
        led5.write(1)
        print (g,f, led5,(Fore.RED+Style.BRIGHT + e)+ Style.RESET_ALL, g,f, g,f, g,f, g,f)
        time.sleep(espera)
        led4.write(1)
        print (g,f, g,f, led4,(Fore.YELLOW+Style.BRIGHT + e)+ Style.RESET_ALL, g,f, g,f, g,f)
        time.sleep(espera)
        led3.write(1)
        print (g,f, g,f, g,f, led3,(Fore.YELLOW+Style.BRIGHT + e)+ Style.RESET_ALL, g,f, g,f)
        time.sleep(espera)
        led2.write(1)
        print (g,f, g,f, g,f, g,f, led2,(Fore.GREEN+Style.BRIGHT + e)+ Style.RESET_ALL, g,f)
        time.sleep(espera)
        led1.write(1)
        print (g,f, g,f, g,f, g,f, g,f, led1,(Fore.GREEN+Style.BRIGHT + e)+ Style.RESET_ALL)
        time.sleep(espera)
        print ("")
        led6.write(0)
        print (Fore.BLACK+Style.BRIGHT, led6,a, led5,a, led4,a, led3,a, led2,a, led1,a)
        led5.write(0)
        print (led6,a, led5,a, led4,a, led3,a, led2,a, led1,a)
        led4.write(0)
        print (led6,a, led5,a, led4,a, led3,a, led2,a, led1,a)
        led3.write(0)
        print (led6,a, led5,a, led4,a, led3,a, led2,a, led1,a)
        led2.write(0)
        print (led6,a, led5,a, led4,a, led3,a, led2,a, led1,a)
        led1.write(0)
        print (led6,a, led5,a, led4,a, led3,a, led2,a, led1,a + Style.RESET_ALL)
        time.sleep(espera)
        print ("")
        led1.write(1)
        print (g,f, g,f, g,f, g,f, g,f, led1,(Fore.GREEN+Style.BRIGHT + e)+ Style.RESET_ALL)
        time.sleep(espera)
        led2.write(1)
        print (g,f, g,f, g,f, g,f, led2,(Fore.GREEN+Style.BRIGHT + e)+ Style.RESET_ALL, g,f)
        time.sleep(espera)
        led3.write(1)
        print (g,f, g,f, g,f, led3,(Fore.YELLOW+Style.BRIGHT + e)+ Style.RESET_ALL, g,f, g,f)
        time.sleep(espera)
        led4.write(1)
        print (g,f, g,f, led4,(Fore.YELLOW+Style.BRIGHT + e)+ Style.RESET_ALL, g,f, g,f, g,f)
        time.sleep(espera)
        led5.write(1)
        print (g,f, led5,(Fore.RED+Style.BRIGHT + e)+ Style.RESET_ALL, g,f, g,f, g,f, g,f)
        time.sleep(espera)
        led6.write(1)
        print (led6,(Fore.RED+Style.BRIGHT + e) + Style.RESET_ALL, g,f, g,f, g,f, g,f, g,f)
        time.sleep(espera)
        print ("")
        led1.write(0)
        print (Fore.BLACK+Style.BRIGHT, led6,a, led5,a, led4,a, led3,a, led2,a, led1,a)
        led2.write(0)
        print (led6,a, led5,a, led4,a, led3,a, led2,a, led1,a)
        led3.write(0)
        print (led6,a, led5,a, led4,a, led3,a, led2,a, led1,a)
        led4.write(0)
        print (led6,a, led5,a, led4,a, led3,a, led2,a, led1,a)
        led5.write(0)
        print (led6,a, led5,a, led4,a, led3,a, led2,a, led1,a)
        led6.write(0)
        print (led6,a, led5,a, led4,a, led3,a, led2,a, led1,a+ Style.RESET_ALL)
        print ("")
    else:
        time.sleep(0.1)


while True:
    poten() #Ejecución infinita hasta finalizar 

