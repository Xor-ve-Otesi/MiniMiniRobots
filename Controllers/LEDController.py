from machine import Pin, PWM, ADC
import time

class LEDController():
    def __init__(self,pins:list) -> None:
        self.pins = pins
        self.LEDs = [Pin(i,Pin.OUT, value = 0) for i in self.pins]
        self.tVal = 2**16 - 2
        # Interrupts
        self.left_button = Pin(14, Pin.IN, Pin.PULL_DOWN)
        self.right_button = Pin(22, Pin.IN, Pin.PULL_UP)


    @staticmethod
    def singleLED(led, value):
        led.value(value)

    def resetLEDs(self):
        for pin in self.pins:
            Pin(pin, Pin.OUT, value=0)

    def multipleLEDs(led, value):
        raise NotImplementedError