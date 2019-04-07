import RPi.GPIO as GPIO

class GpioController:
    def gpio_setup(self, mode):
        GPIO.setmode(mode)

    def set_pin_output(self, pin_number):
        GPIO.setup(pin_number, GPIO.OUT)

    def set_output_high(self, pin_number):
        GPIO.OUT(pin_number, GPIO.HIGH)

    def set_output_low(self, pin_number):
        GPIO.OUT(pin_number, GPIO.LOW)