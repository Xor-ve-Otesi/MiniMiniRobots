from Controllers import LEDController
from machine import Pin, PWM, ADC
import time

class MotorController():
    def __init__(self,pins) -> None:
        self.pins = pins
        self._ledController = LEDController([2,8])
        self.ena = PWM(Pin(pins[0], Pin.OUT))
        self.ena.duty_u16(0)
        self.ena.freq(1000)
        self.in1 = Pin(pins[1], Pin.OUT)
        self.in2 = Pin(pins[2], Pin.OUT)
        self.duty = 0
        self.frequency = 0


    def stop(self):
        self.in1.value(0)
        self.in2.value(0)
        self.ena.duty_u16(0)

    def start(self):
        pass
    
    def forward(self):
        self.in1.value(1)
        self.in2.value(0)

    def backward(self):
        self.in1.value(0)
        self.in2.value(1)
    
    def drive(self):

         while True:
            """
            if self.duty_cycle != self.old_duty:
                self.ena.duty_u16(int(self.duty_cycle / 100 * 65536))
                self.old_duty = self.duty_cycle

            if self.old_frequency != self.frequency:
                self.ena.freq(self.frequency)
                #self.ena.freq(self.frequency)
                self.old_frequency = self.frequency
            """
            pass