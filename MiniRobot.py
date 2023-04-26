from Controllers import ConnectionController, LEDController, MotorController
from machine import Pin, PWM, ADC
import time

class MiniRobot(): 
    def __init__(self) -> None:
        _ledController = LEDController([2,10])
        _motorContoller = MotorController([2,4,5])
        _connectionController = ConnectionController('Galaxy A32AE20','qgfb9519', "192.168.184.141",1234)


    @staticmethod
    def Thermometer():
        sensor_temp = ADC(4)
        # Conversion factor transforms the u16 value read in  to volt value.
        conversion_factor = 3.3 / (65535)

        while True:
            # reading the volt value from the temperature sensor.
            reading = sensor_temp.read_u16() * conversion_factor 
            
            # Temperature sensors sents 0.706 volts while reading 27 degrees celcius.
            # Additionally, 0.001721 voltage is changed with every degree celcius
            # Below line gives the temperature in celcius. 
            temperature = 27 - (reading - 0.706)/0.001721
            print(temperature)
            # Temperature value is displayed.
            time.sleep(2)