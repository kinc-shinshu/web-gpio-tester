import RPi.GPIO as GPIO


class GpioController:
    # set mode
    def gpio_setup(self, mode):
        GPIO.setmode(mode)

    # digital output
    def setup_pin_output_mode(self, pin_number_or_list):
        GPIO.setup(pin_number_or_list, GPIO.OUT)

    def set_output(self, pin_number_or_list, output):
        GPIO.OUT(pin_number_or_list, output)

    # analog output
    # pwmは途中で変更できるため、複数の関数からアクセスできるように変数を先に用意した
    pwm_pin_or_pins = ""

    def setup_pin_pwm_mode(self, pin_number_or_list, frequency):
        self.pwm_pin_or_pins = GPIO.PWM(pin_number_or_list, frequency)

    def start_pwm(self, duty_ratio):
        self.pwm_pin_or_pins.start(duty_ratio)

    def change_pwm_duty_ratio(self, duty_ratio):
        self.pwm_pin_or_pins.ChangeFrequency(duty_ratio)

    def stop_pwn(self, pin_number_or_list):
        self.pwm_pin_or_pins.stop(pin_number_or_list)

    # input
    def read_pin_input(self, pin_number_or_list):
        pin_input = GPIO.input(pin_number_or_list)
        return pin_input

    # cleanup
    def cleanup_pin(self, pin_number_or_list):
        GPIO.cleanup(pin_number_or_list)

    def cleanup_all_pin(self):
        GPIO.cleanup()
